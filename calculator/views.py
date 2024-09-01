from django.shortcuts import render
from . forms import CalculationForm
from django.http import JsonResponse

def calculator_view(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            fabric = form.cleaned_data['fabric']
            quadrature = form.cleaned_data['quadrature']
            installation = form.cleaned_data['installation']
            payment = form.cleaned_data['payment']
            discount = form.cleaned_data['discount']

            total_amount = fabric.price * quadrature + installation
            total_with_discount = total_amount * ((100 - discount) / 100)
            final_amount = total_with_discount * ((100 + payment.percentage) / 100)
            
            data = {
                'success': True,
                'total_amount': total_amount,
                'total_with_discount': total_with_discount,
                'final_amount': final_amount,
            }
            return JsonResponse(data)
        
        return JsonResponse({'success': False, 'errors': form.errors})

    else:
        form = CalculationForm()

    return render(request, 'calculator.html', {
        'form': form
    })
