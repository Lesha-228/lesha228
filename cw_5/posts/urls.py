from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('posts/', posts_view, name='posts'),
    path('posts/my/', my_posts_view, name='my_posts'),
    path('posts/<int:id>/', post_detail_view, name='post_detail'),
    path('posts/create/', create_post_view, name='create_post'),
    path('posts/<int:id>/delete/', delete_post_view, name='delete_post'),
]
