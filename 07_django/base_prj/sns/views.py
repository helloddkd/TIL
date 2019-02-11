from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment
# Create your views here.


def posting_list(request):
    postings = Posting.objects.all()

    return render(request, 'sns/list.html', {'postings': postings})


def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all()

    return render(request, 'sns/detail.html', {'posting': posting, 'comments':comments})


def create_posting(request):
    if request.method == "POST":
        posting = Posting()
        posting.content = request.POST.get('content')
        posting.icon = request.POST.get('icon')
        posting.image = request.FILES.get('image')
        posting.save()

        return redirect('sns:posting_detail', posting.id)
    else:

        return redirect('sns:posting_list')


def edit_posting(request, posting_id):
    posting = Posting.objects.get(id=posting_id)
    if request.method == 'GET':
        icons = {'fas fa-question': '?', 'far fa-smile':':)', 'far fa-angry':':(', 'far fa-smile-wink': ';)', 'far fa-grin-hearts':'♡', }
        return render(request, 'sns/edit.html', {'posting': posting, 'icons': icons })
    else:
        posting.content = request.POST.get('content')
        posting.icon = request.POST.get('icon')
        if request.FILES.get('image'):
            posting.image = request.POST.get('image')
        posting.save()
        return redirect('sns:posting_detail', posting_id)


def delete_posting(request, posting_id):
    if request.method=='POST':
        posting = Posting.objects.get(id=posting_id)
        posting.delete()
        return redirect('sns:posting_list')
    else:
        return redirect('sns:posting_detail', posting_id)


def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method=='POST':
        comment = Comment()
        comment.content = request.POST.get('comment')
        comment.posting = posting
        comment.save()
    return redirect('sns:posting_detail', posting_id)


def delete_comment(request, posting_id, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect('sns:posting_detail', posting_id)
