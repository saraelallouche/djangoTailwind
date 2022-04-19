from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.tmp_storages import CacheStorage

from htmx.models.course import Course, Module


class CourseResource(resources.ModelResource):
    class Meta:
        model = Course


class CourseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ressource_class = CourseResource
    tmp_storage_class = CacheStorage

    list_display = (
        "pk",
        "name",
    )
    search_fields = (
        "pk",
        "name",
    )

    save_on_top = True
    save_as = True


admin.site.register(Course, CourseAdmin)


class ModuleResource(resources.ModelResource):
    class Meta:
        model = Module


class ModuleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ressource_class = ModuleResource
    tmp_storage_class = CacheStorage

    list_display = (
        "pk",
        "name",
        # "course__name",
    )
    search_fields = (
        "pk",
        "name",
        # "course__name",
    )

    save_on_top = True
    save_as = True


admin.site.register(Module, ModuleAdmin)
