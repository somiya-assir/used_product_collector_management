from django.db import models
from Usermanagement.models import User
from Employee.models import Employee


# Create your models here.
class Pickup(models.Model):
    Shedule=models.TimeField()
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)
    employee_name=models.ForeignKey(Employee, on_delete=models.SET_NULL, default=1, null=True)
