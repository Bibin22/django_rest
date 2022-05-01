from rest_framework.response import Response
from watchlist_app.api.serializers import *
# from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics
from watchlist_app.models import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadonly
from .throttling import WatchListThrottlle, WatchListDetails
from .paginations import *
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from rest_framework import status
from rest_framework import viewsets



class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        username = self.request.query_parms.get('username',None)
        return Review.objects.filter(review_user__username=username)
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(review_user__username=username)

#MODELVIEWSET

class StreamPlatformVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer

#VIEWSET


# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self,request):
#         queryset = StreamingPlatform.objects.all()
#         serializer = StreamingPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = StreamingPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamingPlatformSerializer(watchlist)
#         return Response(serializer.data)
#
#     def create(self,request):
#         queryset = StreamingPlatform.objects.all()
#         serializer = StreamingPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)












#GENERIC VIEWS
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review = Review.objects.filter(watchlist=movie, review_user=review_user)
        if review.exists():
            return ValidationError("User Already Exists")

        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            movie.avg_rating =(movie.avg_rating + serializer.validated_data['rating'])/2
        movie.number_rating = movie.number_rating + 1
        movie.save()
        serializer.save(watchlist=movie,  review_user=review_user)

class ReviewList(generics.ListAPIView):

    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class WatchLists(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'platform__name']
    pagination_class = WatchListCPagination

# class ReviewList(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsReviewUserOrReadonly]
    serializer_class = ReviewSerializer


# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#API VIEWS


class StreamingPlatformList(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    def get(self, request):
        stream = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(stream, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamingPlatformDetails(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'streaming_list_detail'
    def get(self, request, id):
        stream = StreamingPlatform.objects.get(id=id)
        serializer = StreamingPlatformSerializer(stream)
        return Response(serializer.data)

    def put(selfself, request, id):
        stream = StreamingPlatform.objects.get(id=id)
        serializer = StreamingPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        stream = StreamingPlatform.objects.get(id=id)
        stream.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class WatchListAPI(APIView):
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [WatchListThrottlle]
    def get(self, request):
        watch_list = WatchList.objects.all()
        serializer = WatchListSerializer(watch_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListDetails(APIView):
    throttle_classes = [WatchListDetails]
    def get(self, request, id):
        watch_list = WatchList.objects.get(id=id)
        serializer = WatchListSerializer(watch_list)
        return Response(serializer.data)

    def put(self, request, id):
        watch_list = WatchList.objects.get(id=id)
        serializer = WatchListSerializer(watch_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        watch_list = WatchList.objects.get(id=id)
        watch_list.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class MovieListAPI(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        movie = Movies.objects.all()
        serializer = MovieListSerializer(movie, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class MovieDetailAPI(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        movie = Movies.objects.get(pk=pk)
        serializer = MovieListSerializer(movie)
        return Response (serializer.data)
    def put(self, request, pk):
        movie = Movies.objects.get(pk=pk)
        serializer = MovieListSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self, request, pk):
        Movies.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
            
        
            

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie = Movies.objects.all()
#         serializer = MovieListSerializer(movie, many=True)
#         print("j", serializer)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
  
    

# @api_view(["GET","PUT", "DELETE"])
# def movie_details(request, pk):
#     if request.method == "GET":
#         try:
#             movie = Movies.objects.get(id=pk)
#         except Movies.DoesNotExist:
#             return Response({"error":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieListSerializer(movie)
#         return Response(serializer.data)
#     if request.method == "PUT":
#         movie = Movies.objects.get(id=pk)
#         serializer = MovieListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method =="DELETE":
#         movie = Movies.objects.get(id=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)