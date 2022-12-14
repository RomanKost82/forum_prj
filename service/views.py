from django.shortcuts import render, redirect
from service.models import Comment, Post
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index(req):
    return render(req, 'index.html')

@login_required
def about(req):
    return render(req, 'about.html')

class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class PostView(ListView):
    
    model = Post
    template_name = "index.html"
    ordering = ['-created_at']

class DetailPostView(DetailView):
    model = Post
    template_name = "detail_post.html"

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "create_post.html"
    form_class = PostForm
   

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "create_post.html"
    form_class = PostForm

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('index')

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "add_comment.html"
    form_class = CommentForm
   
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


    