from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.tmp_storages import CacheStorage

from ..models import CustomUserModel


class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUserModel


class CustomUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ressource_class = CustomUserResource
    tmp_storage_class = CacheStorage

    list_display = (
        "pk",
        "username",
        "lastname",
        "country",
        "created",
        "notifications",
    )
    search_fields = (
        "pk",
        "username",
        "firstname",
        "lastname",
    )

    save_on_top = True
    save_as = True


admin.site.register(CustomUserModel, CustomUserAdmin)
