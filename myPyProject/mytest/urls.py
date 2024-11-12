from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('members/', views.members, name="members"),
    path('mem/<str:pk>/', views.mem, name="mem"),
    path('about_project/', views.about_project, name="about_project"),
]