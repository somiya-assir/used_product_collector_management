from django.shortcuts import render
from .models import Pickup

# Create your views here.
def showpickup(request):

    all = User.objects.all()

    contex = {
        'pickuplist': all
    }
    return render(request, 'usermanagement/userlist.html', contex)

