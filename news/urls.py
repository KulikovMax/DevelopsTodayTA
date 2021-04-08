from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create-news"),
    path("create/saving/", views.save_created, name="create-news-saving"),
    path("upvote/<int:pk>", views.upvote, name="upvote"),
    path("comment/<int:fk>", views.all_comments, name="all-comments"),
    path("comment/<int:fk>/add_comment", views.add_comment, name="add-comment"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
