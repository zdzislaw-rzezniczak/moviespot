from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=180, db_index=True)
    slug = models.SlugField(max_length=180, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mspot:movie_list_by_gatunek', args=[self.slug])


class Movie(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=180, db_index=True)
    rezyser = models.CharField(max_length=180, db_index=True, default='unknown')
    rok_produkcji = models.IntegerField(validators=[MinValueValidator(1900),
                                       MaxValueValidator(2030)], null=True)
    slug = models.SlugField(max_length=180, db_index=True)
    movie_poster = models.ImageField(upload_to='movies/', blank=False, default='posters/brakobrazu.png')
    movie_description = models.TextField(blank=False)
    movie_recenzja = models.TextField(blank=False, default='W tej chwili do tego filmu nie ma dostępnej recenzji')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mspot:movie_detail', args=[self.id, self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Movie,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
