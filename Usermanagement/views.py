from django.shortcuts import render
from .models import User
#Create your views here.
def showuser(request):
    alluser = User.objects.all()

    contex = {
        'userlist': alluser
    }
    return render(request, 'usermanagement/userlist.html', contex)



