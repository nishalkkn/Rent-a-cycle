from django.db import models
from distance_tracking.models import DistanceTracking
from booking.models import Booking

# Create your models here.


class RentAmount(models.Model):
    rent_amount_id = models.AutoField(primary_key=True)
    # distance_tracking_id = models.IntegerField()
    distance_tracking=models.ForeignKey(DistanceTracking,on_delete=models.CASCADE)
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rent_amount'







