from django.shortcuts import render, redirect

from socialapp.models import UserPost
from socialapp.forms import UserPostForm


def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.all()
        form = UserPostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = UserPost(text=text)
            user_post.save()
        return redirect('index')


def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'post_details.html', context)
