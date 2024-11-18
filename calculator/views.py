from django.shortcuts import render
from .forms import CalculationForm
from .models import Icon
from django.http import JsonResponse

def calculator_view(request):
    icon = Icon.objects.first()
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            results = form.cleaned_data['results']
            payment = form.cleaned_data['payment']


            results_with_payment = results * ((100 + payment.percentage) / 100)

            data = {
                'success': True,
                'total_with_payment': results_with_payment,
            }
            return JsonResponse(data)
        
        return JsonResponse({'success': False, 'errors': form.errors})

    else:
        form = CalculationForm()

    return render(request, 'calculator.html', {
        'form': form,
        'icon': icon,
    })
