from rest_framework import serializers
from news.models import News, Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["id", "news", "author_name", "content", "creation_date"]


class NewsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, default=[])

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

    def update(self, instance, validated_data):
        fields = instance._meta.fields
        exclude = []
        for field in fields:
            field = field.name.split('.')[-1]
            if field in exclude:
                continue
            exec("instance.%s = validated_data.get(field, instance.%s)" % (field, field))
        instance.save()
        return instance
