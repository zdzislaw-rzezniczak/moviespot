from decimal import Decimal
from django.conf import settings
from mspot.models import Movie


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):

        movies_ids = self.cart.keys()

        movies = Movie.objects.filter(id__in=movies_ids)

        cart = self.cart.copy()
        for movie in movies:
            cart[str(movie.id)]['movie'] = movie

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, movie, quantity=1, override_quantity=False):

        movie_id = str(movie.id)
        if movie_id not in self.cart:
            self.cart[movie_id] = {'quantity': 0,
                                      'price': str(movie.price)}
        if override_quantity:
            self.cart[movie_id]['quantity'] = quantity
        else:
            self.cart[movie_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, movie):

        movie_id = str(movie.id)
        if movie_id in self.cart:
            del self.cart[movie_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
