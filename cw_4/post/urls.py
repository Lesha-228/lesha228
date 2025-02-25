from django.urls import path
from . import views

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('threads/', views.thread_list, name='thread_list'),
    path('threads/<int:id>/', views.thread_detail, name='thread_detail'),
    path('threads/create/', views.thread_create, name='thread_create'),
]
