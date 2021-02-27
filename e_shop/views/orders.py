from django.shortcuts import render
from django.views import View
from django.http import Http404
from e_shop.models.orders import Order


class OrderView(View):
    def get(self, request):
        user = request.user
        orders = Order.get_orders_by_user(user)
        return render(request, "e_shop/orders.html", {"orders": orders})
