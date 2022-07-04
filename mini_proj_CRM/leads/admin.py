from django.contrib import admin

from .models import User,Lead,Agent

# register the model that would be visible then in the admin panel under Leads section as the app name is Leads
# the string labels coming from the string __init__ method for representing the model inside models.py
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)