from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.tmp_storages import CacheStorage

from ..models import File


class FileResource(resources.ModelResource):
    class Meta:
        model = File


class FileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ressource_class = FileResource
    tmp_storage_class = CacheStorage

    list_display = (
        "pk",
        "name",
        "file",
    )
    search_fields = (
        "pk",
        "name",
        "file",
    )

    save_on_top = True
    save_as = True


admin.site.register(File, FileAdmin)
