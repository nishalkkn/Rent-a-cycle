from django.db import models
from cycle.models import Cycle
from user.models import User

# Create your models here.

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    # cycle_id = models.IntegerField()
    cycle=models.ForeignKey(Cycle,on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.CharField(max_length=45)
    time = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'booking'

