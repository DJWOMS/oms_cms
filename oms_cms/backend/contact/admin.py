from django.contrib import admin

from .models import Contact, ContactSocNet, Feedback, ContactFields, EmailsFeedback


class SocialNetworksAdmin(admin.StackedInline):
    """Соц. сети"""
    model = ContactSocNet
    extra = 1
    show_change_link = True


class ContactFieldsAdmin(admin.StackedInline):
    """Соц. сети"""
    model = ContactFields
    extra = 1
    show_change_link = True


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Контакты"""
    list_display = ("name", "id")
    search_fields = ("id",)
    inlines = (SocialNetworksAdmin, ContactFieldsAdmin)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Обратная связь"""
    list_display = ("full_name", "email", "tel", "theme", "id")
    search_fields = ("theme", "full_name", "email", "tel")
    list_filter = ("id", "theme", "full_name", "email", "tel")


@admin.register(EmailsFeedback)
class EmailsFeedbackAdmin(admin.ModelAdmin):
    list_display = ("email", )
