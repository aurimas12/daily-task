from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    parser_classes = (MultiPartParser, FormParser)
