from django.shortcuts import render
from .models import Payment

# Create your views here.
def showpayment(request):
    all1 = Payment.objects.all()

    contex = {
        'paymentlist': all1
    }
    return render(request, 'payment/payment.html', contex)


