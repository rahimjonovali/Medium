from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .manager import CustomUserManager
from config.model import BaseModel


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="users/avatars/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    headline = models.CharField(max_length=100, null=True, blank=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        import datetime
        today = datetime.date.today()
        return today.year - self.birth_date.year

    objects = CustomUserManager


class Topic(BaseModel):
    title = models.CharField(max_length=100)


# class Story(BaseModel):
#     status_choices = [
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#         ('archive', 'Archive'),
#         ('pending', 'Pending'),
#         ('reject', 'Reject'),
#         ('trash', 'Trash'),
#     ]
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     status = models.CharField(max_length=10, choices=status_choices, default='draft')
#     views_count = models.PositiveIntegerField(default=0)
#     topics = models.ManyToManyField(Topic)
#
#     @property
#     def read_time(self):
#         word_count = len(self.content.split())
#         result = round(word_count / 60)
#         return result
#
#     def __str__(self):
#         return self.title
#
#
# class ReadStory(BaseModel):
#     story = models.ForeignKey(Story, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#
#
# class Clap(models.Model):
#     story = models.ForeignKey(Story, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     count = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
#
#
# class Comment(BaseModel):
#     comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     message = models.TextField()
#
#     def __str__(self):
#         return f'Comment by {self.user.username} on {self.created_at}'
#
#
# class FollowToTopic(BaseModel):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#
#
# class FollowAuthor(BaseModel):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
