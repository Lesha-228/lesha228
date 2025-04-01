from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm


def login_page(request):
    return render(request, 'todos/login.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todos:list')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def todos_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos_list.html', {'todos': todos})


@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todo_detail.html', {'todo': todo})


@login_required
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:list')
    else:
        form = TodoForm()
    return render(request, 'create_todo.html', {'form': form})


@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos:list')
    return render(request, 'delete_todo.html', {'todo': todo})
