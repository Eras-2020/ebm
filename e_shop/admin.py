from django.contrib import admin
from django.utils.html import format_html
from e_shop.models.product import Product, ProductImages
from e_shop.models.category import Category
from e_shop.models.orders import Order
from e_shop.models.company_settings import Setting
from e_shop.models import Blog, BlogCategory,Comment
from e_shop.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created_on', 'status']
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'topic', 'comment']


class SettingAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'created_on']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "phone", "order_date", "product", "quantity", "price", "total", "payment_method",
                    "ip", "status"]
    readonly_fields = (
        "user", "address", "phone", "order_date", "product", "quantity", "price", "total", "payment_method", 'ip')


class ProductImageAdmin(admin.StackedInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', "added_on", "size", 'get_price', 'get_discount', 'get_sale_price', 'get_image']
    inlines = [ProductImageAdmin]

    def get_image(self, obj):
        return format_html(f'''
                <img height='80px' src='{obj.image.url}'/>
            ''')

    def get_sale_price(self, obj):
        sale = format((obj.price - (obj.price * (obj.discount / 100))), '.2f')
        return f'Ksh. {sale}'

    def get_price(self, obj):
        return 'Ksh. ' + str(obj.price)

    def get_discount(self, obj):
        return str(obj.discount) + " %"

    get_sale_price.short_description = "Sale Price"
    get_discount.short_description = "Discount"
    get_price.short_description = "Price"
    get_image.short_description = "Image"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.site_title = "EBM - Company"
admin.site.site_header = "EBM - Company"
admin.site.index_title = ""
