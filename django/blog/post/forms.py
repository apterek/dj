from django import forms
from post.models import Post


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    age = forms.IntegerField(min_value=18, required=False)


class AddPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
