from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/thread_list.html', {'threads': threads})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts})

def thread_create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'post/thread_form.html', {'form': form})

