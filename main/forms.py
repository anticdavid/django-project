from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Post, Comment, Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profession = forms.CharField(required=True)
   
    class Meta:
        model = User
        fields = ["username","email","profession", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]

class UpdateUserForm(forms.ModelForm):
    profession = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["email","username","profession"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']