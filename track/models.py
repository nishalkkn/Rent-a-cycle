from django.db import models

# Create your models here.

class Track(models.Model):
    track_id = models.AutoField(primary_key=True)
    booking_id = models.IntegerField()
    location = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'track'
