from django.contrib import admin
from .models import Zamowienie, ElementyZamowienia

class OrderItemInline(admin.TabularInline):
    model = ElementyZamowienia
    raw_id_fields = ['movie']


@admin.register(Zamowienie)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'imie', 'nazwisko', 'mail',
                    'adres', 'kod_pocztowy', 'miejscowosc', 'oplacone',
                    'data_utworzenia', 'aktualizacja']
    list_filter = ['oplacone', 'data_utworzenia', 'aktualizacja']
    inlines = [OrderItemInline]

