from django.urls import path
from .views.home import Index
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.product_details import ProductDetail
from .views.blog import BlogView, BlogDetails, comment
from .views.contact import contact
from .views.about import About

app_name = 'e_shop'
urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('cart/', Cart.as_view(), name='cart'),
    path("check-out", CheckOut.as_view(), name="checkout"),
    path("orders", OrderView.as_view(), name='orders'),
    path('<int:id>/', ProductDetail.as_view(), name='product_details'),
    path('blog', BlogView.as_view(), name='blog'),
    path("blog_details/<int:id>/", BlogDetails.as_view(), name="blog_details"),
    path("comment/<int:id>/", comment, name="comment"),
    path('contact', contact, name='contact'),
    path('about', About.as_view(), name="about"),

]
