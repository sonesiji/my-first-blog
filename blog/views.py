
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


from blog import models


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
           
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)



from django.shortcuts import render, redirect
from .forms import FeedbackForm

# def feedback(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('thank_you')  # Redirect to a thank you page after submission
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback.html', {'form': form})


# # views.py
# from django.shortcuts import render
# from .models import Feedback

# def feedback_status(request):
#     user_email = request.user.email  # Assuming users are logged in and have an email field
#     feedback = Feedback.objects.filter(email=user_email)
#     return render(request, 'feedback_status.html', {'feedback': feedback})
# def thank_you_view(request):
#     return render(request, 'thank_you.html')
# views.py
from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a thank you page after submission
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_status(request):
    if request.user.is_superuser:  # Check if the user is an admin
        feedback = Feedback.objects.filter(status='Reviewed')
    else:
        user_email = request.user.email  # Assuming users are logged in and have an email field
        feedback = Feedback.objects.filter(email=user_email)
    return render(request, 'feedback_status.html', {'feedback': feedback})

def thank_you_view(request):
    return render(request, 'thank_you.html')

from django.shortcuts import render
from .models import Post
from django.db.models import Q 

def search_results(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(text__icontains=query)
    )
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search_results.html', context)