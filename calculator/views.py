from django.shortcuts import render
from . forms import CalculationForm
from django.http import JsonResponse

def calculate_discount(total_amount):
    if 1000 <= total_amount < 10000:
        return 5
    elif 10000 <= total_amount < 20000:
        return 10
    elif 20000 <= total_amount < 30000:
        return 15
    elif 30000 <= total_amount <40000:
        return 17
    elif 40000 <= total_amount < 50000:
        return 20
    
    return 0
    

def calculator_view(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            fabric = form.cleaned_data['fabric']
            quadrature = form.cleaned_data['quadrature']
            installation = form.cleaned_data['installation']
            payment = form.cleaned_data['payment']

            fabric_price = fabric.price if fabric else 0
            total_amount = fabric_price * quadrature + installation
            discount = calculate_discount(total_amount)
            total_with_discount = total_amount * ((100 - discount) / 100)
            final_amount = total_with_discount * ((100 + payment.percentage) / 100)
            
            data = {
                'success': True,
                'total_amount': total_amount,
                'total_with_discount': total_with_discount,
                'final_amount': final_amount,
                'discount': discount,
            }
            return JsonResponse(data)
        
        return JsonResponse({'success': False, 'errors': form.errors})

    else:
        form = CalculationForm()

    return render(request, 'calculator.html', {
        'form': form
    })
