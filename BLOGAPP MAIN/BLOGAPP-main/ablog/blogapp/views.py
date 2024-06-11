from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogapp/home.html', context)



# @login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
            else:
                # Create a default user account for non-authenticated users
                default_user, _ = User.objects.get_or_create(username='guest')
                post.author = default_user
            post.save()
            return redirect('blogapp:home')
    else:
        form = PostForm()
    return render(request, 'blogapp/post_form.html', {'form': form})


# @login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogapp:home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blogapp/post_form.html', {'form': form})

# @login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blogapp:home')
    return render(request, 'blogapp/post_confirm_delete.html', {'post': post})