from django.shortcuts import render,redirect
from  .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    form = TodoForm()
    if request.method =="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

            title=form.cleaned_data['title']
            task=form.cleaned_data['task']
            user = request.user

            todo=Todo(title=title,task=task,author=user)
            todo.save()

            tasks = list(Todo.objects.filter(author = user).order_by("completed","-updated"))
            return render (request,"home.html",{
            "form":form,
            "msg":"Submited Successesfully",
            "tasks":tasks
            
            })
    
    tasks = list(Todo.objects.filter(author = request.user).order_by("completed","-updated"))
    return render (request,"home.html",{
        "form":form,
        'tasks':tasks
    })

@login_required
def deleteTask(request,pk):
    if request.method == "POST":
        obj = Todo.objects.get(author = request.user,id = pk)
        obj.delete()
        return redirect("home")
    return redirect("home")

@login_required
def completeTask(request,pk):
    if request.method == "POST":
        obj = Todo.objects.get(author = request.user,id = pk)
        obj.completed = True
        obj.save()
        return redirect("home")
    return redirect("home")


@login_required
def notCompleteTask(request,pk):
    if request.method == "POST":
        obj = Todo.objects.get(author = request.user,id = pk)
        obj.completed = False
        obj.save()
        return redirect("home")
    return redirect("home")
@login_required
def editTask(request,pk):
    if request.method == "POST":
        obj = Todo.objects.get(author = request.user,id = pk)
        form = TodoForm()
        return render(request, "edit.html",{
            "task":obj,
            "form":form
        })

@login_required
def saveEditForm(request,pk):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            obj = Todo.objects.get(author =request.user , id = pk)
            obj.title = form.cleaned_data['title']
            obj.task = form.cleaned_data['task']
            obj.save()
            return redirect("home")
