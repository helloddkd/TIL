from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import *
from .forms import PostModelForm, ImageModelForm, CommentModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from IPython import embed
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

            #create HashTag #hi #ssafy #20층
            content = post_form.cleaned_data.get('content')
            words = content.split()
            for word in words:
                if word[0] == '#':
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word)  #(HashTagObj, True)    (HashTagObj, False) 없어서만들었음
                    post.tags.add(tag[0])
                    if tag[1]:
                        messages.add_message(request, messages.SUCCESS, f'#{tag[0].content}를 처음으로 추가하셨어요!')

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
                #update HashTag
                post.tags.clear()
                content = post_form.cleaned_data.get('content')
                words = content.split()
                for word in words:
                    if word[0] == '#':
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(
                            content=word)  # (HashTagObj, True)    (HashTagObj, False) 없어서만들었음
                        post.tags.add(tag[0])
                        if tag[1]:
                            messages.add_message(request, messages.SUCCESS, f'#{tag[0].content}를 처음으로 추가하셨어요!')
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
    if request.is_ajax():
        user = request.user
        post = get_object_or_404(Post, id=post_id)
        is_active = True
        if user in post.like_users.all():
            post.like_users.remove(user)
            is_active = False
        else:
            post.like_users.add(user)
        return JsonResponse({'likeCount': post.like_users.count(), 'is_active':is_active})
    else:
        return HttpResponseBadRequest()


def tag_posts(request, tag):
    tag = get_object_or_404(HashTag, content=tag)
    posts = tag.posts.all()
    form = CommentModelForm()
    return render(request, 'posts/list.html', {'posts': posts, 'form':form})
