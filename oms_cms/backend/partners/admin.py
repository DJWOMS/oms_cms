from django.contrib import admin

from .models import Partners


@admin.register(Partners)
class HotelRoomsAdmin(admin.ModelAdmin):
    """Номера отеля"""
    list_display = ("link",)
    search_fields = ("link",)
