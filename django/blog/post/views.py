from django.shortcuts import render, redirect
import logging
from django.http import HttpResponse
from post.models import Post
from post.forms import RegistrationForm, AddPostForm

logger = logging.getLogger(__name__)


def index(request):
    title = request.GET.get("title")

    if title is None:
        return HttpResponse('Go away')

    post_list = Post.object.filter(title__contains=title)
    post_ids = [post.id for post in post_list]
    return HttpResponse('')


def register(request):
    form = RegistrationForm()
    logger.info(request.POST)
    return render(request, "register.html", {"form": form})


def all_post(request):
    post = Post.objects.all()
    return render(request, "all_post.html", {"post": post})


def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return redirect("add_post")
    else:
        form = AddPostForm()

    return render(request, "add_post.html", {"form": form})
