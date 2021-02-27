from django.views import View
from django.shortcuts import render
from e_shop.models import Setting


class About(View):
    def get(self, request):
        setting = Setting.objects.get(pk=1)

        return render(request, 'e_shop/about.html', {'setting': setting})
