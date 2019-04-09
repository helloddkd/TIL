from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed #이건 포스트해야하는데 겟요청들어오면 안될때 쓰는거
from .models import Posting, Comment
from django.views.decorators.http import require_http_methods
from datetime import datetime

# Create your views here.
# Read
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'board_ad/list.html', {
        'postings': postings
    })

def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    # comments = Posting.comment_set.all()
    comments = Comment.objects.filter(posting=posting).order_by('-created_at')
    return render(request, 'board_ad/detail.html', {
        'posting': posting,
        'comments': comments,
    })

# Create
def posting_create(request):
    if request.method == 'POST':
        posting = Posting()
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', posting_id=posting.id)
    else:
        return render(request, 'board_ad/new.html')

# Update
@require_http_methods(['GET','POST'])
def posting_update(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        posting.title = request.POST.get('posting_title')
        posting.content = request.POST.get('posting_content')
        posting.save()
        return redirect('board_ad:posting_detail', posting_id=posting.id)
    else:
        return render(request, 'board_ad/update.html', {
            'posting': posting
        })

# Delete
@require_http_methods(['POST'])
def posting_delete(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('board_ad:posting_list')


#Comment - create
@require_http_methods(['POST'])
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = Comment()
    comment.posting = posting
    comment.content = request.POST.get('comment')
    comment.save()
    return redirect('board_ad:posting_detail', posting_id)

@require_http_methods(['POST'])
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment,id=comment_id)
    comment.delete()
    return redirect('board_ad:posting_detail', posting.id)

@require_http_methods(['GET', 'POST'])
def update_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment,id=comment_id)
    if request.method == 'GET':
        return render(request, 'board_ad/comment_update.html', {'posting':posting, 'comment':comment})
    else:
        comment.content  =request.POST.get('comment')
        comment.save()
        return redirect('board_ad:posting_detail', posting.id)
