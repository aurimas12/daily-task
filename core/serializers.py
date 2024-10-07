from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='image', read_only=True)

    class Meta:
        model = MyModel
        fields = ['id', 'name', 'image', 'image_url']

    def get_image_url(self, obj):
        return obj.get_image_path()
