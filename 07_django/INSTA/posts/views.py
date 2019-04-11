from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Post
from .forms import PostModelForm
# Create your views here.

@require_GET
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})


@require_http_methods(['GET', 'POST'])
def create_post(request):
    #get 방식으로 data를 입력할 form 요청
    if request.method == 'POST':
        # post 방식으로 넘어온 데이터를 모델폼에 넣는다.
        form = PostModelForm(request.POST, request.FILES)
        # data 검증을 한 번 한다.
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
    else:
        form = PostModelForm()
    return render(request, 'posts/form.html', {'form':form})


@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
    else: form = PostModelForm(instance=post)
    return render(request, 'posts/form.html', {
        'form': form,
    })


@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('posts:post_list')

