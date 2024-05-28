from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, PostForm, UpdateForm, UpdateUserForm, CommentForm, ProfilePictureForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Post, Profile, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# - Home

@login_required(login_url='/login')
def home(request):
    posts_list = Post.objects.all()

    p = Paginator(Post.objects.all(), 4)
    page = request.GET.get('page')
    posts = p.get_page(page)

    if request.method == 'POST':
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request, 'main/home.html', {'posts_list': posts_list,  'posts': posts})

# - Create a Post

@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()
    
    return render(request, 'post/create_post_form.html', {"form":form})

# - Update a Post

@login_required(login_url='/login')
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form  = UpdateForm(instance=post)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/home")
    return render(request, 'post/update_post_form.html', {"form":form})

# - View/Read a single Post

@login_required(login_url='/login')
def view_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST' and 'comment-id' in request.POST:
        comment_id = request.POST.get('comment-id')
        comment = get_object_or_404(Comment, id=comment_id, post=post)
        if request.user == comment.user:
            comment.delete()
            return redirect('view_post', pk=pk)

    return render(request, 'post/view_post.html', {"post":post})
 
# - Sign up

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()

            profession  = form.cleaned_data['profession']

            profile = Profile.objects.create(user=user,profession=profession)
            profile.bio = user.username
            profile.save()

            login(request,user)
            
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form":form})

#View a Profile

def view_profile(request):
    user_profile = request.user.profile
    return render(request, 'profile/view_profile.html', {'user_profile': user_profile})

# Update a User

@login_required(login_url='/login')
def update_user(request, pk):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)
    form = UpdateUserForm(request.POST or None, instance=user, initial={"profession": profile.profession})

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            profile.profession = form.cleaned_data['profession']
            profile.save()
            return redirect("/view_profile")

    return render(request, 'profile/update_profile_form.html', {"form": form})

# Add a Comment

@login_required(login_url='/login')
def add_comment(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect('view_post', pk=post.id)
    else:
        form = CommentForm()
    
    return render(request, 'post/add_comment.html', {'form': form, 'post': post})

# Update a Comment

def update_comment(request, pk, comment_id):
    post = get_object_or_404(Post, id=pk)
    comment = get_object_or_404(Comment, id=comment_id, post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('view_post', pk=pk)
    else:
        form = CommentForm(instance=comment)

    return render (request, 'post/update_comment.html', {'form':form, 'comment':comment})

# Upload a Profile photo

@login_required
def upload_profile_pic(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')  
    else:
        form = ProfilePictureForm(instance=request.user.profile)
    return render(request, 'profile/upload_profile_pic.html', {'form': form})