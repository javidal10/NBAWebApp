from django.db import models


class Player(models.Model):
    """
    This model will create a table with args: first name,lastname,heigth inches,height in meters
    will return by default only the name of player
    """
    first_name = models.CharField(max_length=30,null=False)
    last_name = models.CharField(max_length=20,null=False)
    h_in = models.IntegerField(null=False)
    h_meters = models.FloatField(null=False)

    def __str__(self):
        return str(self.first_name)+' '+str(self.last_name)
    