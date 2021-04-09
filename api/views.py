from rest_framework import generics
from rest_framework.generics import get_object_or_404

from news.models import News, Comments
from .serializers import NewsSerializer, CommentsSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        news = News.objects.get(pk=self.kwargs['id'])
        comments = Comments.objects.filter(news=news)
        if serializer.is_valid():
            serializer.save(comments=comments)


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentsList(generics.ListCreateAPIView):
    def get_queryset(self):
        news = News.objects.get(pk=self.kwargs["pk"])
        return Comments.objects.filter(news=news)

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return get_object_or_404(
            queryset=self.get_queryset(), id=self.kwargs.get("comment_pk")
        )

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
