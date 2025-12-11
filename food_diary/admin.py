from django.contrib import admin, messages
from django.http import HttpResponse
import csv
from django.utils import timezone

from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    """Admin for Food model with common list/search/filter helpers.

    When creating a Food in the admin, if the `user` field is left blank
    it will be set to the current admin user.
    """
    list_display = ("name", "meal_type", "date", "user", "reviewed")
    list_display_links = ("name",)
    list_editable = ("meal_type", "reviewed")
    list_filter = ("meal_type", "date", "user", "reviewed")
    search_fields = ("name", "user__username", "user__email")
    readonly_fields = ("date",)

    fieldsets = (
        (None, {
            "fields": ("name", "meal_type", "user")
        }),
        ("Timestamps", {
            "fields": ("date",),
        }),
    )

    def save_model(self, request, obj, form, change):
        # If creating a new object and user not specified, set to current user
        if not change and (not getattr(obj, "user", None)):
            obj.user = request.user
        super().save_model(request, obj, form, change)

    actions = [
        "export_as_csv",
        "mark_as_reviewed",
        "mark_as_unreviewed",
        "bulk_delete",
    ]

    def export_as_csv(self, request, queryset):
        """Export selected Food rows as CSV."""
        field_names = [
            "id",
            "name",
            "meal_type",
            "date",
            "user",
            "reviewed",
        ]

        response = HttpResponse(content_type="text/csv")
        ts = timezone.now().strftime("%Y%m%d_%H%M%S")
        filename = f"food_export_{ts}.csv"
        response["Content-Disposition"] = (
            "attachment; filename=" + filename
        )

        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow(
                [
                    obj.pk,
                    obj.name,
                    obj.meal_type,
                    obj.date,
                    getattr(obj.user, "username", ""),
                    obj.reviewed,
                ]
            )

        return response
    export_as_csv.short_description = "Export selected as CSV"

    def mark_as_reviewed(self, request, queryset):
        updated = queryset.update(reviewed=True)
        self.message_user(
            request,
            f"Marked {updated} entries as reviewed.",
            messages.SUCCESS,
        )
    mark_as_reviewed.short_description = "Mark selected items as reviewed"

    def mark_as_unreviewed(self, request, queryset):
        updated = queryset.update(reviewed=False)
        self.message_user(
            request,
            f"Marked {updated} entries as not reviewed.",
            messages.SUCCESS,
        )
    mark_as_unreviewed.short_description = (
        "Mark selected items as not reviewed"
    )

    def bulk_delete(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(
            request,
            f"Deleted {count} selected Food items.",
            messages.SUCCESS,
        )
    bulk_delete.short_description = "Delete selected Food items"
