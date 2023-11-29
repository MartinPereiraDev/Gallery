from django.urls import path,include

from rest_framework.routers import DefaultRouter

from art_space import admin

from .views import GalleryPut, GalleryListPost

app_name = "art_space"

router = DefaultRouter()


urlpatterns = [
    path("",         GalleryListPost.as_view(), name='gallery'),
    path("<int:pk>/", GalleryPut.as_view({'get':'retrieve', 'put': 'update'}), name='gallery_put'),
    
]