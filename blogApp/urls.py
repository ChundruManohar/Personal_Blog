from blogApp.views import *   # Add this line     
from django.urls import path

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]
