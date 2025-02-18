from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def redirect_to_lists(request):
    return redirect('todo_lists')

def todo_lists(request):
    lists = TodoList.objects.all()
    form = TodoListForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('todo_lists')
    return render(request, 'todos/todo_lists.html', {'lists': lists, 'form': form})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    form = TodoForm(request.POST or None, initial={'todo_list': todo_list})
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('todo_list_detail', id=id)
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos, 'form': form})

def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')

def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    form = TodoListForm(request.POST or None, instance=todo_list)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('todo_lists')
    return render(request, 'todos/edit_todo_list.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', id=todo_list_id)

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('todo_list_detail', id=todo.todo_list.id)
    return render(request, 'todos/edit_todo.html', {'form': form})

