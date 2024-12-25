from django.db import models

class Payment(models.Model):
    payment = models.CharField(verbose_name='Оплата', max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Процент', default=0)

    def __str__(self):
        return self.payment
    
    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'


class Icon(models.Model):
    icon = models.ImageField(upload_to='data/', verbose_name='Логотип')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return self.description
    

class Term(models.Model):
    term = models.IntegerField(verbose_name='Срок')

    def __str__(self):
        return f'{self.term} месяц'