from django.shortcuts import render, redirect
from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm

# Create your views here.

def list(request):
    postings = Posting.objects.all()
    form = PostingModelForm()
    return render(request, 'sns/list.html', {'postings': postings, 'form':form})


def delete_posting(request):
    pass


def create_posting(request):
    if request.method == 'POST':
        form = PostingModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sns:list')
    return redirect('sns:list')


def create_comment(request):
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        pass


def posting_detail(request, posting_id):
    posting = Posting.objects.get(id=posting_id)
    return render(request, 'sns/detail.html', {'posting':posting})
