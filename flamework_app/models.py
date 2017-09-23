from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    pass


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=32, null=False)
    description = models.TextField(null=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        get_latest_by = 'updated_at'


class IdeaImage(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateTimeField(null=False, auto_now=True)


class EngineerIdea(Idea):
    pass


class DesignerIdea(Idea):

    def __str__(self):
        return self.title


class Like(models.Model):
    liked_to = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", related_query_name="like",)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'created_at'
