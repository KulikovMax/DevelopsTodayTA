from django.urls import path

from . import views

urlpatterns = [
    path("", views.NewsList.as_view()),
    path("<int:pk>/", views.NewsDetail.as_view()),
    path("<int:pk>/comments/", views.CommentsList.as_view()),
    path("<int:pk>/comments/<int:comment_pk>/", views.CommentsDetail.as_view()),
]
