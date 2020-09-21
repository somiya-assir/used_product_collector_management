from django.db import models
from Usermanagement.models import User
from Buyer.models import Buyer

class Userproduct(models.Model):
    product_type=models.CharField(max_length=100)
    weight=models.IntegerField(blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)

    User= models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)
    Buyer= models.ForeignKey(Buyer, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
      return self.product_type
