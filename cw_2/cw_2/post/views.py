
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()  # Получение всех записей
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('post_list')

# Create your views here.
