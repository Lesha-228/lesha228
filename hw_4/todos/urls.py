from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_lists, name='todo_lists'),
    path('<int:id>/', views.todo_list_detail, name='todo_list_detail'),
    path('<int:id>/delete/', views.delete_todo_list, name='delete_todo_list'),
    path('<int:id>/edit/', views.edit_todo_list, name='edit_todo_list'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
    path('todos/<int:id>/edit/', views.edit_todo, name='edit_todo'),
]

