from rest_framework.response import Response
from watchlist_app.api.serializers import MovieListSerializer, WatchListSerializer, StreamingPlatformSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import *
from rest_framework import status


class StreamingPlatformList(APIView):
    def get(self, request):
        stream = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(stream, many=True )
        return Response(serializer.data)
    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamingPlatformDetails(APIView):
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