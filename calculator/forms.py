from django import forms
from .models import Payment, Term

class CalculationForm(forms.Form):
    results = forms.IntegerField(
        label='Общая сумма',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите сумму заказа'})
    )

    prepayment = forms.IntegerField(
        label='Предоплата',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':' Введите предоплату'})
    )

    payment = forms.ModelChoiceField(
        queryset=Payment.objects.all(),
        label='Оплата',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    term = forms.ModelChoiceField(
        queryset=Term.objects.all(),
        label='Срок',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
