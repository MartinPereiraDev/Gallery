from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.parsers import MultiPartParser

from .models import Gallery
from .serializers import GallerySerializer


# view File put and get archive gallery
class GalleryPut(viewsets.ModelViewSet):
    """
        This endpoints show only one element of Gallery.
        RETRIEVE and PUT.    
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    parser_classes = (MultiPartParser,)



# class gallery Post, Put 
class GalleryListPost(generics.ListCreateAPIView):
    """
    This view lists gallery and create Post  
    
    """
    queryset = Gallery.objects.all()
    serializer_class    = GallerySerializer

#class GalleryDowlnload(generics.)