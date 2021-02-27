from django.views import View
from django.shortcuts import render, redirect
from e_shop.models import Product,ProductImages


class ProductDetail(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        images = ProductImages.objects.filter(product=product.id)

        data = {'product':product,'images':images}
        return render(request, 'e_shop/product_details.html', data)

    def post(self, request, id):
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
        return redirect('e_shop:product_details', id=id)