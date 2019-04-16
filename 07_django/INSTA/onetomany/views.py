from django.shortcuts import render, redirect
from .forms import *
from .models import Book, Writer, Chapter
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = WriterModelForm(request.POST) #html갈때는 빈종이! 다시 밑에 렌더하면 찬종이!
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = WriterModelForm()
    return render(request, 'new.html', {'form':form})


def update(request, id):
    writer = Writer.objects.get(id=id)
    if request.method == 'POST':
        form = WriterModelForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect()
    else:
        form = WriterModelForm(instance=writer)
    return render(request, 'edit.html', {'form':form})

