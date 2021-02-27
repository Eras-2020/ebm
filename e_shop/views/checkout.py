from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from e_shop.models import Product, Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user = request.user
        cart = request.session.get('cart')
        payment_method = request.POST.get('payment_method')
        products = Product.get_products_by_id(list(cart.keys()))
        print(user, phone)
        for product in products:
            order = Order(user=User(id=user.id),
                          product=product,
                          price=round((product.price - (product.price * (product.discount / 100)))),
                          address=address,
                          payment_method=payment_method,
                          phone=phone,
                          quantity=cart.get(str(product.id)),
                          total=round((product.price - (product.price * (product.discount / 100)))) * cart.get(
                              str(product.id)),
                          ip=request.META.get('REMOTE_ADDR'),
                          )
            order.save()
        request.session['cart'] = {}
        return redirect('e_shop:orders')

    def get(self, request):
        products = Product.objects.all()
        return render(request, "e_shop/check-out.html", {'products': products})
