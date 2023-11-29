from django.urls import path,include

from rest_framework.routers import DefaultRouter

from art_space import admin

from .views import GalleryView, GalleryListPost

app_name = "art_space"

router = DefaultRouter()


urlpatterns = [
  #  path('admin/', admin.site.urls),
   #path('', AgreementFileView.index, name='index'),
    path("gallery/", GalleryView.as_view({'get':'retrieve'}), name='gallery'),
    path("art/",         GalleryListPost.as_view(), name='art'),
]