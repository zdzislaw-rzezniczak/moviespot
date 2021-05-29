from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mspot.models import Movie
from .cart import Cart
from .forms import CartAddMovieForm


@require_POST
def cart_add(request, movie_id):
    cart = Cart(request)
    movie = get_object_or_404(Movie, id=movie_id)
    form = CartAddMovieForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(movie=movie,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, movie_id):
    cart = Cart(request)
    movie = get_object_or_404(Movie, id=movie_id)
    cart.remove(movie)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddMovieForm(initial={'quantity': item['quantity'],
                                                                 'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})
