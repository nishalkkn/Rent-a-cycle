from django.db import models
from rent_amount.models import RentAmount

# Create your models here.

class Payment(models.Model):
    payment = models.AutoField(primary_key=True)
    # rent_amount_id = models.IntegerField(blank=True, null=True)
    rent_amount=models.ForeignKey(RentAmount,on_delete=models.CASCADE)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'
