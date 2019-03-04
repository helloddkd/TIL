from django.shortcuts import render, redirect
from .models import Posting

def index(request):
    postings = Posting.objects.all()
    return render(request, 'board/index.html', {'postings':postings})

def detail(request, posting_id):
    posting = Posting.objects.get(id=posting_id)
    return render(request, 'board/detail.html', {'posting':posting})

def delete(request, posting_id):
    if request.method == 'POST':
        posting = Posting.objects.get(id=posting_id)
        posting.delete()
    return redirect('board:index')


