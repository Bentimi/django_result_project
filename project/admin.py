from django.contrib import admin
from . models import user
from import_export.admin import ImportExportModelAdmin
# from import_export import resources
# Register your models here.

admin.site.register(user, ImportExportModelAdmin)
# admin.site.register(Services, ImportExportModelAdmin)

