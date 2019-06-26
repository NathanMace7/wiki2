from django.contrib import admin

from .models import Page, UserFileUpload

#These pages require admin priveleges
admin.site.register(Page)
admin.site.register(UserFileUpload)

