from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',obtain_auth_token, name='login'),
    path('logout/',logout_view, name='logout'),
    path('registration/',registration_view, name='registration'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]