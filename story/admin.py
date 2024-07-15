from django.contrib import admin
from .models import *


admin.site.register(Story)
admin.site.register(Topic)
admin.site.register(FollowToTopic)
admin.site.register(FollowAuthor)
admin.site.register(Clap)
admin.site.register(Comment)
admin.site.register(ReadStory)