from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup')
]