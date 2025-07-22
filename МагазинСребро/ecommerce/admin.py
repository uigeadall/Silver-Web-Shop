from django.contrib import admin
from .models import Category, Product, CartItem, Order, OrderItem, Favorite


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Favorite)