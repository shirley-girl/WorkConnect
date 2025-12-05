from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile,name='profile'),
    path('login/', views.loginUser, name ='login'),
    path('register/jobseeker', views.register_jobseeker, name= 'register_jobseeker'),
    path('register/employer', views.register_employer, name='register_employer'),
    path('logout', views.logoutUser, name='logout'),
]




