from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    parser_classes = (MultiPartParser, FormParser)

from django.conf import settings
from django.http import JsonResponse
from pathlib import Path
import os

def list_images(request):
    images_dir = Path(settings.MEDIA_ROOT) / 'images'
    image_files = [f.name for f in images_dir.iterdir() if f.is_file()]

    image_paths = [settings.MEDIA_URL + 'images/' + image for image in image_files]

    return JsonResponse({'images': image_paths})
