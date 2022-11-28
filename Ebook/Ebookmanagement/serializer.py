from rest_framework import serializers
from .models import ebook 
class ebookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ebook
        fields = ['url', 'title', 'author', 'genre','review','favourite']