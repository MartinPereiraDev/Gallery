from django.db import models

from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model

User = get_user_model()



# validate files work (jpg, png)   
def validate_file_image(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File type not supported. Please upload a .jpg or .png file.')

# model gallery
class Gallery(models.Model):
    author          = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='author')
    work_title      = models.CharField(max_length=50, name='title')
    work            = models.FileField(upload_to='albums/images/', validators=[validate_file_image])


    def __str__(self):
        return self.work_title