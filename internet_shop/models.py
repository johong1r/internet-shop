from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} - {self.id}'


class Brand(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return f'{self.name} - {self.id}'


class Goods(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.CharField(max_length=1000, verbose_name="Описание")
    price = models.IntegerField(verbose_name='Цена')
    is_active = models.BooleanField(verbose_name='В наличие', default=True)
    picture = models.ImageField(null=True, blank=True, verbose_name='Фотография')
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name='Категория', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=True, blank=True, verbose_name='Бренд', on_delete=models.CASCADE)
    size = models.CharField(max_length=1000, verbose_name="Размер")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} - {self.id}'


class OrderItem(models.Model):
    goods = models.ForeignKey(Goods, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество', default=1)
    price = models.IntegerField(verbose_name='Цена')
    cart = models.ForeignKey('Order', verbose_name='Корзина', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return f'OrderItem: {self.goods.name} (x{self.quantity})'
    

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    user = models.ForeignKey(OrderItem, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order #{self.id} - {self.items}'