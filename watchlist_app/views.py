# from django.shortcuts import render
# from .models import *
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movies.objects.all()
#     data = {
#         "movies":list(movies.values())
#     }
#     print(list(movies.values()))
#     return JsonResponse(data)


# def movie_details(request, pk):
#     movie = Movies.objects.get(id=pk)
#     print(movie)
#     data = {
#         'name':movie.name,
#         'description':movie.description,
#         'active': movie.active
        
#     }
#     return JsonResponse(data)
