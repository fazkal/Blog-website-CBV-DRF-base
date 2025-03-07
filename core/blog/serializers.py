from rest_framework import serializers
from .models import Post, Category
from accounts.models import Profile


# Serializer for Category
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


# Serializer for Post
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "category",
            "status",
            "created_date",
            "published_date"
        ]
        # Set author read_only_fields to prevent the post creator from changing
        read_only_fields = ["author"]

    # Get the owner of the post created from request
    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)