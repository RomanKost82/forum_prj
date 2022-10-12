from django.forms import ModelForm, fields, widgets
from .models import Post, Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "title": forms.TimeInput(attrs={'class':'form-control'}),
            "desc": forms.Textarea(attrs={'class':'form-control'}),
            }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["desc"]
        widgets = {
                "desc": forms.Textarea(attrs={'class':'form-control'}),
            }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
