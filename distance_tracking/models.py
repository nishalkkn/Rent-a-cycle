from django.db import models
from booking.models import Booking

# Create your models here.

class DistanceTracking(models.Model):
    distance_tracking_id = models.AutoField(primary_key=True)
    # booking_id = models.IntegerField()
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    start_point = models.CharField(max_length=45)
    end_point = models.CharField(max_length=45)
    distance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'distance_tracking'

