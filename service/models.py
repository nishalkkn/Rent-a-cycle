from django.db import models
from Shop.models import Shop

# Create your models here.

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    # render_id = models.IntegerField()
    render=models.ForeignKey(Shop,on_delete=models.CASCADE)
    service = models.CharField(max_length=45)
    charge = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service'

