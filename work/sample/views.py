
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import TaskForm

def fetch(request):
    var=list(Task.objects.all().values())
    form=TaskForm
    d1={'form': form,
        'data': var }
    return render(request,"index.html",d1)

#def dis(request):
   # return render(request,"index.html")

def view(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        Task.objects.create(**form.cleaned_data)
    
    return redirect(fetch)

def delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect(fetch)
