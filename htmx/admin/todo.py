from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.tmp_storages import CacheStorage

from htmx.models.todo import Todo


class TodoResource(resources.ModelResource):
    class Meta:
        model = Todo


class TodoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ressource_class = TodoResource
    tmp_storage_class = CacheStorage

    list_display = (
        "pk",
        "title",
        "is_done",
    )
    search_fields = (
        "pk",
        "title",
        "is_done",
    )

    save_on_top = True
    save_as = True


admin.site.register(Todo, TodoAdmin)
