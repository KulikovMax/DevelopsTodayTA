from rest_framework import serializers
from news.models import News, Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["id", "news", "author_name", "content", "creation_date"]


class NewsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True)

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
            "comments",
        ]
