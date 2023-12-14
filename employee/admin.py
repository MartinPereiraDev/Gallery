from django.contrib import admin

from .models import Employee

admin.site.site_header = 'Gallery Site Admin'

# class for list and filters 
class GalleryAdmin(admin.ModelAdmin):

    #show files up 
    list_display = ['name', 'work_in', 'email' ]

    #filter for list 
    list_filter = ['work_in', 'surname']

    # links for link show display one 
    list_display_links = ['name']

    #search by files
    search_fields = ('surname',)

    list_per_page = 5
    

admin.site.register(Employee, GalleryAdmin)
