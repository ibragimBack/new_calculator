from django import forms
from .models import Goods_Fabric, Payment, Discount

class CalculationForm(forms.Form):
    fabric = forms.ModelChoiceField(
        queryset=Goods_Fabric.objects.all(),
        label='Ткань',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    quadrature = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Квадратура',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите квадратуру'})
    )

    installation = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Установка',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите стоимость установки'})
    )

    payment = forms.ModelChoiceField(
        queryset=Payment.objects.all(),
        label='Оплата',
        widget=forms.Select(attrs={'class': 'form-control'}))

    discount = forms.ModelChoiceField(
        queryset=Discount.objects.all(),
        label='Скидка',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
