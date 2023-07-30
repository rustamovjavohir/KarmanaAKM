from rest_framework import serializers

from apps.books.models import Image, Category


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'is_main', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'parent', 'image', 'is_event', 'created_at', 'updated_at')
