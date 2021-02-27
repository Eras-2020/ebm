from django.shortcuts import render, redirect
from django.views import View
from e_shop.models.product import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get("cart").keys())
        products = Product.get_products_by_id(ids)
        return render(request, "e_shop/cart.html", {"products": products})

    def post(self, request):
        clear = request.POST.get('clear')
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        if clear:
            request.session['cart'] = {}
        return redirect('e_shop:cart')

