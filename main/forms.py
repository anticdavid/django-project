from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Post, Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email","username", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name","email","username"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")