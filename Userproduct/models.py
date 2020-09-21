from django.db import models

class Userproduct(models.Model):
    product_type=models.CharField(max_length=100)
    weight=models.IntegerField(blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)

    def __str__(self):
      return self.product_type
