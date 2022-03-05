from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.tmp_storages import CacheStorage

from ..models import Post


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ressource_class = PostResource
    tmp_storage_class = CacheStorage

    list_display = (
        "pk",
        "title",
        "author",
        "body",
    )
    search_fields = (
        "pk",
        "title",
        "author",
        "body",
    )

    save_on_top = True
    save_as = True


admin.site.register(Post, PostAdmin)
