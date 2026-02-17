from django.contrib import admin
from .models import Country, Currency, Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Country)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Currency)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)

