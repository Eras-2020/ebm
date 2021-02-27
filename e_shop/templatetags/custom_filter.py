from django import template

register = template.Library()


@register.filter(name="currency")
def currency(number):
    return "Ksh. " + str(number)


@register.filter(name="multiply")
def multiply(product, quantity):
    return quantity * getSalePrice(product)


@register.filter(name='sale_price')
def getSalePrice(product):
    return product.price - (product.price * (product.discount / 100))
