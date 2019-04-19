from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Post, Image, Comment
from .forms import PostModelForm, ImageModelForm, CommentModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@require_GET
def post_list(request):
    posts = Post.objects.all()
    form = CommentModelForm()
    return render(request, 'posts/list.html', {'posts': posts, 'form': form})


@login_required
@require_http_methods(['GET', 'POST'])
def create_post(request):
    if request.method == 'POST':
        post_form = PostModelForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:post_list')
    else:
        post_form = PostModelForm()
    image_form = ImageModelForm()
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user: #지금 수정하려는 post 작성자가 요청보낸 사람이냐?
        if request.method == 'POST':
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('posts:post_list')
        else:
            post_form = PostModelForm(instance=post)
        return render(request, 'posts/form.html', {
            'post_form': post_form,
        })
    else:
        return redirect('posts:post_list')


@login_required
@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('posts:post_list')

@login_required
@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentModelForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentModelForm()
    return render(request, 'posts/form.html', {'post_form': form})


@require_POST
def delete_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@require_POST
@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if user in post.like_users.all():
    # if post.like_users.get(id=user.id).exist():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
