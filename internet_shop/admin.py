from django.contrib import admin
from .models import Goods, Category, Brand, OrderItem, Order


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_active', 'category', 'brand')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'category', 'brand')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'goods', 'quantity')
    list_display_links = ('id', 'goods')
    search_fields = ('goods__name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    list_display_links = ('id',)
    search_fields = ('id',)