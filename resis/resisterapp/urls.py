from django.contrib import admin
from django.urls import path
from resisterapp import views

urlpatterns = [
    
    path('',views.SingupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout',views.LogoutPage,name='logout'),
]