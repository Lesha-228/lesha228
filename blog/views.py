from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(post__id=post_id, author=self.request.user)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_id, author=self.request.user)
        serializer.save(author=self.request.user, post=post)
        
def post_list_view(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    comments = Comment.objects.filter(post=post, author=request.user)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    comments = Comment.objects.filter(post=post, author=request.user)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

@login_required
def post_list(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/post_list.html', {'posts': posts})

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
def get_queryset(self):
    return Comment.objects.filter(post_id=self.kwargs['post_pk'])