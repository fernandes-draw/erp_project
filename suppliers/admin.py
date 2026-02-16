from django.contrib import admin

from suppliers.models import Country, Currency


@admin.register(Country)
class UnitMeasureAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Currency)
class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
