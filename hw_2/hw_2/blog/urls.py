from django.urls import path
from .views import article_list, article_detail
from django.urls import path, include

urlpatterns = [
    path('', include('post.urls')),
]


urlpatterns = [
    path('articles/', article_list),
    path('articles/<int:article_id>/', article_detail),
    
]
