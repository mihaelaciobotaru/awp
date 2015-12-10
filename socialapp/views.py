from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from socialapp.forms import UserPostForm, UserPostCommentForm, UserLoginForm
from socialapp.models import UserPost, UserPostComment


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)


class EditPostView(LoginRequiredMixin, UpdateView):
    model = UserPost
    fields = ['text']
    template_name = 'edit_post.html'


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = UserPost
    template_name = 'delete_post.html'

    def get_success_url(self):
        return reverse('index')


class PostListView(LoginRequiredMixin, ListView):
    model = UserPost
    form_class = UserPostForm
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = UserPost(text=text, author=request.user)
            user_post.save()
        return redirect('index')


@login_required
def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)
    if request.method == 'GET':
        form = UserPostCommentForm()
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'post_details.html', context)
    elif request.method == 'POST':
        form = UserPostCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment = UserPostComment(text=text, post=post, author=request.user)
            comment.save()
        return redirect('post_details', pk=pk)


def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'login.html', context)
        else:
            login(request, user)
            return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')
