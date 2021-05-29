from django.db import models
from mspot.models import Movie


class Zamowienie(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    mail = models.EmailField()
    adres = models.CharField(max_length=250)
    kod_pocztowy = models.CharField(max_length=20)
    miejscowosc = models.CharField(max_length=100)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    aktualizacja = models.DateTimeField(auto_now=True)
    oplacone = models.BooleanField(default=False)

    class Meta:
        ordering = ('-data_utworzenia',)

    def __str__(self):
        return 'Zamowienie {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class ElementyZamowienia(models.Model):
    zamowienie = models.ForeignKey(Zamowienie,
                                   related_name='items',
                                   on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,
                              related_name='order_items',
                              on_delete=models.CASCADE)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    ilosc = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.cena * self.ilosc
