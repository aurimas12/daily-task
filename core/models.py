from django.db import models
import os
from django.conf import settings

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_image_path(self):
        image_path = os.path.join(settings.MEDIA_ROOT, 'images', self.image.name)

        if os.path.exists(image_path):
            return os.path.join(settings.MEDIA_URL, 'images', self.image.name)
        else:
            return None
