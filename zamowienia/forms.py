from django import forms
from .models import Zamowienie


class FormularzZamowienia(forms.ModelForm):
    class Meta:
        model = Zamowienie
        fields = ['imie', 'nazwisko', 'mail', 'adres',
                  'kod_pocztowy', 'miejscowosc']
