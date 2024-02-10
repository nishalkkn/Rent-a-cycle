from django.db import models

# Create your models here.

class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'shop'

