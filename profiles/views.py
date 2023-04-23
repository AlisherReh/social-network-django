
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import SearchForm, StatusForm

from django.contrib.auth.decorators import login_required

from .models import Status, User
from posts.models import Post

@login_required(login_url = 'login')
def profiles_list_view(request):
    profiles = User.objects.all()
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(username__icontains=query))
    
    return render(request, "profiles/profile_list.html", {"profiles": profiles, 'form': form, 'results': results})

@login_required(login_url = 'login')
def my_profile_view(request):
    posts = Post.objects.filter(user = request.user)

    followers = Status.objects.filter(followers=request.user)
    profile = request.user.status
    follows = profile.followers.all()
    
    context = {'follows': follows, 'followers':followers, 'posts': posts}
    return render(request, 'profiles/myprofile.html', context)

@login_required(login_url = 'login')
def profile_view(request, id):
    try:
        profile = Status.objects.get(id=id)
        followers = Status.objects.filter(followers = profile.user)
        follow_check = request.user.status 
        user = profile.user
        if user in follow_check.followers.all():
            button_text = 'Unfollow'
        else:   
            button_text = 'Follow'
        context = {'profile':profile, 'button_text': button_text, 'followers':followers}
        return render(request, 'profiles/profile.html', context)
    except Status.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

@login_required(login_url = 'login')
def follow_func(request, id):
    
    follow_check = request.user.status
    user_follow_status = Status.objects.get(id=id)
    user = user_follow_status.user
    if user in follow_check.followers.all():
        follow_check.followers.remove(user)
    else:   
        follow_check.followers.add(user)
    
    return redirect('profiles:profile-view', id)
    


@login_required(login_url='login')
def edit_status_view(request):
    status = request.user.status
    if request.method == 'POST':
        form = StatusForm(request.POST, request.FILES, instance=status)
        if form.is_valid():
            form.save()
            return redirect('profiles:my-profile-view')
    else:
        form = StatusForm(instance=status)
    return render(request, 'profiles/edit_status.html', {'form': form})

@login_required(login_url='login')
def postDelete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('profiles:my-profile-view')
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")