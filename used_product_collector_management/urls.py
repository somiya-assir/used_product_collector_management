"""used_product_collector_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from Usermanagement import views as user_views
from Userproduct import views as product_views
from Pickup import views as pickup_views
from Payment import views as pay_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_list/',user_views.showuser,name='user_list'),
    path('product_list/',product_views.showproduct,name='product_list'),
    path('pickup_list/',pickup_views.showpickup,name='pickup_list'),
    path('payment_list/', pay_views.showpayment, name='pay_list'),

]
