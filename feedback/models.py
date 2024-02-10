from django.db import models
from user.models import User
from Shop.models import Shop

# Create your models here.

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # render_id = models.IntegerField()
    render=models.ForeignKey(Shop,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'feedback'
