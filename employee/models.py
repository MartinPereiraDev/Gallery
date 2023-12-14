from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Employee(models.Model):
    class EmployeeRol(models.TextChoices):
        DIRECTOR    = 'D'
        MAINTENANCE = 'M'
        SECURITY    = 'S'
        MARKETING   = 'MK'
        INVESTIGADOR = 'I'
        DEVELOPER    = 'DV'
        SELLER       = 'SL'    
        NOT_ASIGNED    = 'NT'   


    name = models.CharField(
            max_length=30
        )
    surname = models.CharField(
            max_length=30
        )

        #textchoice related at Space asigned employee 
    work_in = models.CharField(
        choices=EmployeeRol.choices, max_length=2, default=EmployeeRol.NOT_ASIGNED
    )
    email = models.EmailField(null=False)
    
    adress = models.CharField(
        null=True, blank=True, max_length=45
    )
    country = models.CharField(
        null=True, blank=True, max_length=40
    )
    city = models.CharField(
        null=True, blank=True, max_length=45
    )

    #social network
    linkedin    = models.URLField(null=True, blank=True)
    facebook    = models.URLField(null=True, blank=True)
    twitter     = models.URLField(null=True, blank=True)  

    def __str__(self):
     return self.name
    
    class Meta:
        verbose_name_plural = 'Admin Employee'   