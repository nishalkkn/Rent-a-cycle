from django.db import models
from Shop.models import Shop

# Create your models here.

class Cycle(models.Model):
    cycle_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    size = models.CharField(max_length=45)
    rent_amount = models.FloatField()
    # render_id = models.IntegerField()
    render=models.ForeignKey(Shop,on_delete=models.CASCADE)
    image = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'cycle'
