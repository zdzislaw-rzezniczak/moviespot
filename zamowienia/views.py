from django.shortcuts import render
from cart.cart import Cart
from .models import ElementyZamowienia
from .forms import FormularzZamowienia


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = FormularzZamowienia(request.POST)
        if form.is_valid():
            zamowienie = form.save()
            for item in cart:
                ElementyZamowienia.objects.create(zamowienie=zamowienie,
                                         movie=item['movie'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()

            return render(request,
                          'created.html',
                          {'zamowienie': zamowienie})
    else:
        form = FormularzZamowienia()
    return render(request,
                  'create.html',
                  {'cart': cart, 'form': form})
