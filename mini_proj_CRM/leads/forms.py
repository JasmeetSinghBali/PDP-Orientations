from django import forms
from .models import Lead

# 📝: model Form
class LeadModelForm(forms.ModelForm):
    # meta class where we specify the information about the form
    class Meta:
        model = Lead # model we are using
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        ) # tupple of fields in the form that are


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)