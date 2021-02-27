from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render
from e_shop.models.contact import Message, ContactForm
from e_shop.models.company_settings import Setting


def contact(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Message()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Message sent successfully, Thank you.")
            return HttpResponseRedirect('/contact')
    setting = Setting.objects.get(pk=1)
    customer = request.session.get('customer')
    form = ContactForm
    context = {'form': form, 'setting': setting, 'customer': customer}
    return render(request, 'e_shop/contact.html', context)
