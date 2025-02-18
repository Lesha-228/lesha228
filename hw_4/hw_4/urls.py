"""
URL configuration for hw_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todos import views  

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.redirect_to_lists, name='home'),  
    path('todo-lists/', views.todo_lists, name='todo_lists'),
    path('todo-lists/<int:id>/', views.todo_list_detail, name='todo_list_detail'),
    path('todo-lists/<int:id>/delete/', views.delete_todo_list, name='delete_todo_list'),
    path('todo-lists/<int:id>/edit/', views.edit_todo_list, name='edit_todo_list'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
    path('todos/<int:id>/edit/', views.edit_todo, name='edit_todo'),
]

