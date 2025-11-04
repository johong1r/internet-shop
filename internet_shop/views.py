from django.shortcuts import render, redirect, get_object_or_404
from .models import Goods, Brand, Category
from django.views.generic import TemplateView, DetailView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        goods = Goods.objects.filter(is_active=True)
        
        brand_id = self.request.GET.get('brand')
        category_id = self.request.GET.get('category')
        
        if brand_id:
            goods = goods.filter(brand_id=brand_id)
        if category_id:
            goods = goods.filter(category_id=category_id)
        
        context['goods'] = goods
        context['brands'] = Brand.objects.all()
        context['categories'] = Category.objects.all()
        
        return context


class GoodsDetailView(DetailView):
    model = Goods
    template_name = 'goods_detail.html'
    context_object_name = 'goods'


def add_to_cart_view(request, pk):
    goods = get_object_or_404(Goods, pk=pk)
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(pk), {'quantity': 0, 'name': goods.name, 'price': goods.price})
    cart_item['quantity'] += 1
    cart[str(pk)] = cart_item
    request.session['cart'] = cart
    return redirect('index')


def cart_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart_view(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('cart')


def clear_cart_view(request):
    request.session['cart'] = {}
    return redirect('cart')


