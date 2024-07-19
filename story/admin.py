from django.contrib import admin
from .models import *


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at')
    list_display_links = ('id','title')
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at')
    list_display_links = ('id','title','created_at')
admin.site.register(Story,StoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(FollowToTopic)
admin.site.register(FollowAuthor)
admin.site.register(Clap)
admin.site.register(Comment)
admin.site.register(ReadStory)