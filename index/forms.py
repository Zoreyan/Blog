from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput'
                }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'floatingImage'
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'floatingArea',
                'rows': '5',
                'style': 'resize: vertical;'
                })
        }

class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput'
            }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput'
            }),
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput'
                }),
        }