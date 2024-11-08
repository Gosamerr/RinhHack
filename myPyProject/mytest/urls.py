from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('members/', views.members, name="members"),
    path('mem/<str:pk>/', views.mem, name="mem"),
]