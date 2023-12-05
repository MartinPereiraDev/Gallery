from django.shortcuts import render
from django.http import FileResponse


from rest_framework import viewsets, generics
from rest_framework.views import APIView
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


# class gallery download file 
class GalleryDownload(APIView):
    """
        this view is for download file work with pk of gallery 
    """
    def get(self, request, gallery_id):
        #query
        art_gallery_sign_obj = Gallery.objects.get(id=gallery_id)
        #path
        art_gallery_sign_path = art_gallery_sign_obj.work.path
        #open file
        response = FileResponse(open(art_gallery_sign_path, 'rb'))
    
        response['Content-Disposition'] = f'attachment; filename="{art_gallery_sign_obj.work}"'
        return response

