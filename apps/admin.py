from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Users, Params

from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin


@admin.register(Users)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'age',)

@admin.register(Params)
class ParamsAdmin(ImportExportModelAdmin):
    list_select_related = ('user', )