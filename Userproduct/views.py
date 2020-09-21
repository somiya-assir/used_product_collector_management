from django.shortcuts import render
from .models import Userproduct

# Create your views here.
def showproduct(request):

    allproduct = Userproduct.objects.all()

    contex = {
        'list': allproduct
    }
    return render(request, 'product/userproduct.html', contex)

