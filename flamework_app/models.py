from django.db import models
from django.contrib.auth.models import AbstractUser
import requests
import uuid


class User(AbstractUser):
    pass


class UserInfo(models.Model):
    ENGINEER = 'engineer'
    DESIGNER = 'designer'
    USER_TYPE = (
        (ENGINEER, 'エンジニア'),
        (DESIGNER, 'デザイナー'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.CharField(max_length=16, null=False, choices=USER_TYPE, default=ENGINEER)
    weekday_daytime = models.BooleanField(null=False, default=False)
    weekday_night = models.BooleanField(null=False, default=False)
    weekends_daytime = models.BooleanField(null=False, default=False)
    weekends_night = models.BooleanField(null=False, default=False)
    address = models.CharField(max_length=32, null=False, blank=False)
    zipcode = models.CharField(max_length=16, null=False, blank=False)

    def digest_address(self, address):
        url = 'http://zipcoda.net/api'
        r = requests.get(url, params={'address': address})
        self.zipcode = r.json()['items'][0]['zipcode']
        r = requests.get(url, params={'zipcode': self.zipcode})
        self.address = r.json()['items'][0]['address']
        self.save()

    def get_zip_distance(self, other):
        if self.zipcode == other:
            return 0
        for distance in range(1, len(self.zipcode)):
            if self.zipcode[:-distance] == other[:-distance]:
                return distance
        return len(self.zipcode)


class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=32, null=False)
    description = models.TextField(null=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        get_latest_by = 'updated_at'

    @property
    def images(self):
        return IdeaImage.objects.filter(idea=self)

    @property
    def image_num(self):
        return IdeaImage.objects.filter(idea=self).count()


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
