from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
# Create your views here.
def main (request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'post_main.html', ctx)

def create (request):
    if request.method == "GET":
        form = PostForm()
        ctx  = {
            'form': form,
        }
        return render (request, 'post_create.html', ctx)
    
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect ('post:main')
    else:
        ctx = {
            'form': form,
        }
        return render(request, 'post:create', ctx)
    
    
def detail (request, pk):
    post = Post.objects.get(id = pk)
    post_comments = Comment.objects.filter(post=post)
    ctx = {
        'post': post,
        'comments': post_comments
    }
    return render (request, 'post_detail.html', ctx)

def update (request, pk):
    post = Post.objects.get(id = pk)
    if request.method == "GET":
        form = PostForm(instance = post)
        ctx = {
            'form': form,
        }
        return render (request, 'post_update.html', ctx)
    else :
        post.title = request.POST['title']
        post.content = request.POST['content']
        
        post.save() 
        return redirect("post:detail", pk)

def delete (request, pk):
    if request.method == "POST":
        post = Post.objects.get (id = pk)
        post.delete()
    return redirect ("post:main")

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like(request):
    req = json.loads(request.body)
    post_id = req['id']
    post = Post.objects.get(id=post_id)

    if post.isLiked:
        post.isLiked = False
        post.like -= 1
    else:
        post.isLiked = True
        post.like += 1

    post.save()

    return JsonResponse({'id': post_id, 'isLiked': post.isLiked, 'likeCount': post.like})

@csrf_exempt
def comment(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        post_id = req.get('id')
        post_comment = req.get('comment')
        if post_id and post_comment:
            try:
                post = Post.objects.get(id=post_id)
                comment = Comment(post=post, content=post_comment)
                comment.save()
                return JsonResponse({'status': 'success'})
            except Post.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Post does not exist'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        
        
@csrf_exempt
def get_comments(request, pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(post__id=pk)
        serialized_comments = [{'id': comment.id, 'content': comment.content} for comment in comments]
        return JsonResponse(serialized_comments, safe=False)

    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def delete_comment(request, postId, commentId):
    if request.method == "POST":
        post = Post.objects.get(id = postId)
        comment = Comment.objects.filter (id = commentId, post = post)
        comment.delete()
        return JsonResponse({'message': '댓글이 삭제되었습니다.'})