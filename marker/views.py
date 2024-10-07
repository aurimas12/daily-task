from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from pathlib import Path
import os

# Create your views here.
def list_images(request):
    images_dir = Path(settings.MEDIA_ROOT) / 'images'
    image_files = [f.name for f in images_dir.iterdir() if f.is_file()]

    image_paths = [settings.MEDIA_URL + 'images/' + image for image in image_files]

    return JsonResponse({'images': image_paths})
