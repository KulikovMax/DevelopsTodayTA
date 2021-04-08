from django.contrib import admin
from .models import News, Comments


class NewsAdmin(admin.ModelAdmin):
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
