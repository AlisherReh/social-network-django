import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post,Comments
from profiles.models import Status, User
from django.contrib.auth.decorators import login_required
from project1.decorators import allowed_users, admin_only
from .forms import PostForm, CommentForm
from django.http import JsonResponse
from django.core.paginator import Paginator
@login_required(login_url = 'login')
def posts_page(request):

    posts = Post.objects.order_by(('-created'))

    profile = get_object_or_404(Status, user=request.user)

    post_form = PostForm()
    comment_form = CommentForm()
    
    if request.method == 'POST':
        if 'submit_post' in request.POST:
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('posts:posts')
        
    
    paginator = Paginator(posts, 5)
    
    page = request.GET.get('page')

    posts = paginator.get_page(page)
    
    context = {
        'posts': posts,
        'profile': profile,
        'post_form': post_form,
        'comment_form': comment_form,
    }
    return render(request, 'posts/main.html', context)

@login_required(login_url = 'login')
def following_posts_page(request):
    
    profile = get_object_or_404(Status, user=request.user)

    following_users = profile.followers.all()
    posts = Post.objects.filter(user__in=following_users).order_by(('-created'))
    post_form = PostForm()
    comment_form = CommentForm()
    
    if request.method == 'POST':
        if 'submit_post' in request.POST:
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('posts:posts')
        
    
    paginator = Paginator(posts, 5)
    
    page = request.GET.get('page')

    posts = paginator.get_page(page)
    
    context = {
        'posts': posts,
        'profile': profile,
        'post_form': post_form,
        'comment_form': comment_form,
    }
    return render(request, 'posts/main.html', context)

@login_required(login_url = 'login')
def save_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        postid = request.POST['postid']
        post = Post.objects.get(id=postid)
        user = request.user
        
        datetime_obj = datetime.datetime.now()

        hour = datetime_obj.strftime("%I")
        minute = datetime_obj.strftime("%M")

        # Determine whether it's AM or PM
        am_or_pm = "a.m." if datetime_obj.strftime("%p") == "AM" else "p.m."

        # Format the datetime manually
        formatted_datetime = "{}:{:02d} {}".format(hour, int(minute), am_or_pm)

        # Get the month and day components
        month = datetime_obj.strftime("%B")
        day = datetime_obj.strftime("%d")
        year = datetime_obj.strftime("%Y")

        # Combine the formatted datetime with month, day, and year
        time = "{}, {} {}, {}".format(month, day, year, formatted_datetime)
        
        imgurl = request.POST['imageurl']

        Comments.objects.create(
            comment_body = comment,
            post = post,
            user = user
        )
        return JsonResponse({'bool':True, 'time':time, 'imgurl':imgurl})


