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
