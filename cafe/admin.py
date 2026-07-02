from django.contrib import admin

from .models import CafeInfo, Category, ContactMessage, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ("name", "description", "price", "is_veg", "is_featured", "is_available", "order")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "tagline", "order", "item_count")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("order",)
    inlines = [MenuItemInline]

    @admin.display(description="Items")
    def item_count(self, obj):
        return obj.items.count()


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_veg", "is_featured", "is_available", "order")
    list_filter = ("category", "is_veg", "is_featured", "is_available")
    list_editable = ("price", "is_featured", "is_available", "order")
    search_fields = ("name", "description")
    autocomplete_fields = ()


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at", "handled")
    list_filter = ("handled", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "phone", "message", "created_at")
    list_editable = ("handled",)

    def has_add_permission(self, request):
        return False  # messages only arrive via the contact form


@admin.register(CafeInfo)
class CafeInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Singleton: only allow one row.
        return not CafeInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.site_header = "Wow Weffles Admin"
admin.site.site_title = "Wow Weffles Admin"
admin.site.index_title = "Manage your café"
