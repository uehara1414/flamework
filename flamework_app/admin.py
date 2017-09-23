from django.contrib import admin
from flamework_app.models import User, UserInfo, IdeaImage, EngineerIdea, DesignerIdea, Like
# Register your models here.

admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(IdeaImage)
admin.site.register(EngineerIdea)
admin.site.register(DesignerIdea)
admin.site.register(Like)
