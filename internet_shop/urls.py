from .views import IndexView, GoodsDetailView, cart_view, add_to_cart_view, remove_from_cart_view, clear_cart_view, checkout_view, order_history_view
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('goods/<int:pk>/', GoodsDetailView.as_view(), name='goods_detail'),
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:pk>/', add_to_cart_view, name='add_to_cart'),
    path('cart/remove/<int:pk>/', remove_from_cart_view, name='remove_from_cart'),
    path('cart/clear/', clear_cart_view, name='clear_cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('orders/history/', order_history_view, name='order_history'),
]
