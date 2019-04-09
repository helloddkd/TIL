from django.shortcuts import render, redirect
from .models import Posting

def posting_list(request):
    postings = Posting.objects.all()
    render(request, 'board_ad/list.html', {'postings':postings})


def posting_detail(request, id):
    posting = Posting.objects.get(id=id)
    render(request, 'board_ad/detail.html', {'posting': posting})
