import re
from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.

def home(request):
    if request.method=='POST':
        title=request.POST['todo']
        start=request.POST['start']
        finish=request.POST['finish']
        new=Todo(title=title,start=start,finish=finish)
        new.save()
        return redirect('/')
    todos=Todo.objects.all()
    context={
        'todos':todos
    }
    return render(request,'index.html',context=context)

def deletetodo(request,id):
    todo=Todo.objects.filter(id=id).delete()
    return redirect('/')

def finishtodo(request,id):
    last=Todo.objects.get(id=id)
    inkor=not(last.status)
    todo=Todo.objects.filter(id=id).update(status=inkor)
    return redirect('/')

def updatetodo(request,id):
    if request.method=='POST':
        title=request.POST['todo']
        start=request.POST['start']
        finish=request.POST['finish']
        new=Todo.objects.filter(id=id).update(title=title,start=start,finish=finish)
        return redirect('/')
    todo=Todo.objects.filter(id=id)
    context={
        'todo':todo
    }
        
    return render(request,'update.html',context=context)
        
    