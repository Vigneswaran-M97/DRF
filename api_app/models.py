from django.db import models

class Phonelist(models.Model):
    model_name = models.CharField(max_length=255)
    model_number = models.IntegerField()
    model_year = models.IntegerField()
    model_detail = models.CharField(max_length=255)
    class Meta:
        db_table = "Phonelist"
    
    def __str__(self):
        return self.model_name
        
class BuyPlatforms(models.Model):
    platforms_name = models.CharField(max_length=255)
    model_lunch = models.DateField()
    model_number = models.IntegerField()
    model_price = models.IntegerField()
    class Meta:
        db_table ="BuyPlatforms"

    def __str__(self):
        return self.platforms_name
    