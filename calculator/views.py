from django.shortcuts import render
from .forms import CalculationForm
from .models import Icon
from django.http import JsonResponse

def calculator_view(request):
    icon = Icon.objects.first()  # Получаем первую иконку, если она есть
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            fabric = form.cleaned_data['fabric']
            quadrature = form.cleaned_data['quadrature']
            installation = form.cleaned_data['installation']
            payment = form.cleaned_data['payment']
            discount = form.cleaned_data['discount']

            total_amount = fabric.price * quadrature + installation
            total_with_payment = total_amount * ((100 + payment.percentage) / 100)

            if total_with_payment < discount.min_price or total_with_payment > discount.max_price:
                return JsonResponse({
                    'success': False,
                    'error': f'Такая скидка непозволительно! Скидка для этой суммы: {discount.discount_percentage}%'
                })

            final_amount = total_with_payment * ((100 - discount.discount_percentage) / 100)

            data = {
                'success': True,
                'total_with_payment': total_with_payment,
                'final_amount': final_amount,
                'fabric_price': fabric.price,
            }
            return JsonResponse(data)
        
        return JsonResponse({'success': False, 'errors': form.errors})

    else:
        form = CalculationForm()

    return render(request, 'calculator.html', {
        'form': form,
        'icon': icon
    })
