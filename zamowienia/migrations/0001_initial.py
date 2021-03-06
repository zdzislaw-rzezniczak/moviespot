# Generated by Django 4.0.dev20210403125743 on 2021-05-26 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mspot', '0006_movie_movie_recenzja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('adres', models.CharField(max_length=250)),
                ('kod_pocztowy', models.CharField(max_length=20)),
                ('miejscowosc', models.CharField(max_length=100)),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True)),
                ('aktualizacja', models.DateTimeField(auto_now=True)),
                ('oplacone', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-data_utworzenia',),
            },
        ),
        migrations.CreateModel(
            name='ElementyZamowienia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ilosc', models.PositiveIntegerField(default=1)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='mspot.movie')),
                ('zamowienie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='zamowienia.zamowienie')),
            ],
        ),
    ]
