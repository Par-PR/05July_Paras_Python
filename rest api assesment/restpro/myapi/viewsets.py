from rest_framework import viewsets
from . import models
from . import serializers


class userapiviews(viewsets.ModelViewSet):
    queryset = models.userapi.objects.all()
    serializer_class = serializers.Userapiserializer