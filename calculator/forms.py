from django import forms
from .models import Payment

class CalculationForm(forms.Form):
    results = forms.IntegerField(
        label='Общая сумма',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите сумму заказа'})
    )

    payment = forms.ModelChoiceField(
        queryset=Payment.objects.all(),
        label='Оплата',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

