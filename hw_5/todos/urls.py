from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todos_list, name='list'),
    path('<int:id>/', views.todo_detail, name='detail'),
    path('create/', views.create_todo, name='create'),
    path('<int:id>/delete/', views.delete_todo, name='delete'),
]
