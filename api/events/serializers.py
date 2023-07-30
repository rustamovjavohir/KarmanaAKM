from api.books.serializers import ImageSerializer
from api.auth_user.serializers import UserSerializer
from apps.events.models import Events
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)
    user = serializers.SerializerMethodField(method_name='get_user')
    main_image = serializers.SerializerMethodField(method_name='get_main_image')
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Events
        fields = ('id', 'name', 'main_image', 'description', 'category', 'image', 'user', 'created_at', 'updated_at')

    def get_main_image(self, obj):
        request = self.context.get('request')
        if main_image := obj.image.filter(is_main=True).first():
            return request.build_absolute_uri(main_image.image.url)
        return None

    def get_user(self, obj):
        return obj.created_by.full_name
