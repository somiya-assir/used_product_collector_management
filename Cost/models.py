from django.db import models
from Employee.models import Employee
from Userproduct.models import Userproduct

# Create your models here.



class Cost(models.Model):

  amount=models.IntegerField()
  employee_name = models.ForeignKey(Employee, on_delete=models.SET_NULL, default=1, null=True)
  Userproduct = models.ForeignKey(Userproduct, on_delete=models.CASCADE, default=1, null=True)