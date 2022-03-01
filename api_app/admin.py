from pyexpat import model
from django.contrib import admin
from api_app.models import Phonelist, BuyPlatforms
# Register your models here.
model = [Phonelist, BuyPlatforms]
admin.site.register(model)