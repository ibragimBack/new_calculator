from django.db import models

class Goods_Fabric(models.Model):
    fabric = models.CharField(verbose_name='Ткань', max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.fabric
    
    class Meta:
        verbose_name = 'Ткань'
        verbose_name_plural = 'Ткани'


class Payment(models.Model):
    payment = models.CharField(verbose_name='Оплата', max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Процент', default=0)

    def __str__(self):
        return f"{self.payment} ({self.percentage}%)"
    
    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'


class Discount(models.Model):
    min_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Минимальная сумма')
    max_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Максимальная сумма')
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Процент скидки')

    def __str__(self):
        return f"Скидка {self.discount_percentage} на сумму от {self.min_price} до {self.max_price}"
    
    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидка'

class Icon(models.Model):
    icon = models.ImageField(upload_to='data/', verbose_name='Логотип')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return self.description