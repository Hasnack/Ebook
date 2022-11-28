from django.shortcuts import render
from .serializer import ebookSerializer
from .models import ebook
from rest_framework import viewsets
class ebookViewSet(viewsets.ModelViewSet):
    queryset = ebook.objects.all()
    serializer_class = ebookSerializer
# Create your views here.
