from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


# Serializer for Category
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


# Serializer for Post
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    absolute_url = serializers.HyperlinkedIdentityField(
        view_name='blog:api-v1:post-detail')
    author_full_name = serializers.ReadOnlyField(source="get_author_full_name")

    class Meta:
        model = Post
        fields = [
            "id",
            "image",
            "author",
            "author_full_name",
            "title",
            "content",
            "snippet",
            "category",
            "status",
            "absolute_url",
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
    
    # Change the display mode of post info based on the list or detail 
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
        rep["category"] = CategorySerializer(instance.category).data
        return rep