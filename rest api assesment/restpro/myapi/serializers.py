from rest_framework import serializers
from .models import userapi


class Userapiserializer(serializers.ModelSerializer):
    class Meta:
        model = userapi
        fields = '__all__'
        