from django.contrib import admin
from.models import Product, Cart, CartItem, Category, CustomerProfile, Order, OrderItem

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(CustomerProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
