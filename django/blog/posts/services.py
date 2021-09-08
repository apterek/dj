from datetime import timedelta

from django.utils import timezone

from posts.models import Post


first_post = Post.objects.create(title="First post")
second_post = Post(title="First post")
second_post.save()

post_list = Post.objects.all()
single_post = Post.objects.get(id=1)
single_post = Post.objects.filter(id=1).first()
post_list = Post.objects.filter(title__contains="Test")

single_post = Post.objects.get(id=1)
single_post.title = "New title"
single_post.save()

Post.objects.filter(title__contains="Test").update(title="new_test")

single_post = Post.objects.get(id=1)
single_post.delete()
Post.objects.filter(title__contains="Test").delete()

now = timezone.now()
post_list = Post.objects.filter(created_at__gt=now - timedelta(days=2))
