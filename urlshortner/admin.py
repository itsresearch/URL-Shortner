from django.contrib import admin
from .models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ["short_code", "original_url", "user", "clicks", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["short_code", "original_url"]
