from django.db import models
# 📝:IMP get user model is a function to grab user model by django
from django.contrib.auth.models import AbstractUser

# inherit AbstractUser from django
class User(AbstractUser):
    # if u dont intend to add anything new to the baseAbstractClass for user by django
    pass
    #📝 in future if additional schema for user is required it can be added here

class Lead(models.Model):
# Model class props inherited in Lead class so it act as now a model class
    # db model define here

    # SOURCE_CHOICES = (
    #     # the first value gets stored in DB while second is the display value
    #     # its always better to make first value as short abbrevation as it will take less space in DB
    #     ('YT','YouTube'),
    #     ('GOG','Google'),
    #     ('NL','Newsletter'),
    # )
    first_name = models.CharField(max_length=20) # first_name restricts to string of CharField
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0) # whole integer

    # phoned = models.BooleanField(default=False) # boolean value
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100) # multiple choices as tupple NOTE - these values can get overrided though its not a constraint that source only has three possible options

    # profile_picture is optional as we have set blank=True
    # profile_picture = models.ImageField(blank=True,null=True) # blank True means empty string, null means that their is no value in database
    # special_files = models.FileField() # files, it is actually reff to the actual file stored in DB

    #📝 COMPLEX RELATIONSHIPS TABLE COLUMNS
    # FOREIGN KEY
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)# 📝 "Agent" string is written to make ref to the Agent class even if Agent class was declared/defined after the Leads class

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# added user to the Agent as Agent is going to login in the system(CRM) not the leads
class Agent(models.Model):
    # 📝 on_delete=CASCADE so if a user is deleted than that agent will be deleted as well
    # 📝 to have 1-1 relation i.e 1 user has exactly 1 agent related to it we use OneToOneField and it works exactly like forign key just the diff is that the relation is 1-1 strict only rather in case of foreign keys where 1 user could have multiple agents
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #📝:IMP string representation that returns the user email for Agent model when model manager is called on Agent via Agent.objects.all() in shell
    def __str__(self):
        return self.user.email