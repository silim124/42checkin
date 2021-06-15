from django.contrib import admin

from cadet.models import CadetUser

__all__ = [
    "CadetAdmin",
]


class CadetAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "create_time",
    )
    readonly_fields = (
        "name",
        "create_time",
    )
    list_display = (
        "name",
        "is_active",
        "create_time",
    )
    sortable_by = (
        "name",
        "create_time",
    )
    search_fields = (
        "name",
        "is_active",
    )


admin.site.register(CadetUser, CadetAdmin)
