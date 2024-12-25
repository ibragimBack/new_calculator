from django.shortcuts import render, redirect
from .forms import CalculationForm
from .models import Icon

def calculator_view(request):
    icon = Icon.objects.first()
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            results = form.cleaned_data['results']
            payment = form.cleaned_data['payment']
            prepayment = form.cleaned_data['prepayment']
            term = form.cleaned_data['term']

            results_with_payment = results * ((100 + payment.percentage) / 100)
            remainig_sum = results_with_payment - prepayment
            monthly_payment = remainig_sum / term.term

            request.session['results_with_payment'] = int(results_with_payment)
            request.session['monthly_payment'] = int(monthly_payment)
            request.session['months'] = int(term.term)
            request.session['prepay'] = int(prepayment)
            request.session['payment'] = payment.payment

            return redirect('results')

    else:
        form = CalculationForm()

    return render(request, 'calculator.html', {
        'form': form,
        'icon': icon,
    })


def results_view(request):
    results_with_payment = request.session.get('results_with_payment')
    monthly_payment = request.session.get('monthly_payment')
    months = request.session.get('months')
    prepay = request.session.get('prepay')
    payment = request.session.get('payment')
    
    if any(value is None for value in (results_with_payment, monthly_payment, months, prepay, payment)):
        return redirect('calculator')
    
    return render(request, 'results.html', {
        'results_with_payment': results_with_payment,
        'monthly_payment': monthly_payment,
        'months': months,
        'prepay': prepay,
        'payment': payment,
        })