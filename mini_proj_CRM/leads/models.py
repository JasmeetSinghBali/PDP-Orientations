from django.db import models

# Model class props inherited in Lead class so it act as now a model class
class Lead(models.Model):
    # db model define here
    first_name = models.CharField(max_length=20) # first_name restricts to string of CharField
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0) # whole integer