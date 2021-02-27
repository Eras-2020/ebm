from django.views import View
from django.shortcuts import render, redirect
from e_shop.models.product import Product
from e_shop.models.category import Category
from e_shop.models import Setting


class Index(View):
    def post(self, request):
        product =  request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity =  cart.get(product)
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
        return redirect('e_shop:home')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        categories = Category.objects.all()
        categoryID = request.GET.get('category')
        setting = Setting.objects.get(id=1)
        random_products = Product.objects.all().order_by('?')[:3]
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.objects.all()
            setting = Setting.objects.get(id=1)
            random_products = Product.objects.all().order_by('?')[:3]

        print("You are: " + str(request.user))
        data = {'products': products, 'categories': categories, 'setting':setting, 'random_products': random_products}
        return render(request, 'e_shop/index.html', data)
