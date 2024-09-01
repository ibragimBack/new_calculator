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