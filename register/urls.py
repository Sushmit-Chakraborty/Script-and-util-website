from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginUser,name='loginUser'),
    path('signup',views.registerUser,name='registerUser'),
    path('logout',views.logoutUser,name='logoutUser')
]