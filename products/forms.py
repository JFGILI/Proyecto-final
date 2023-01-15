from django import forms

class LocationForm(forms.Form):
    name = forms.CharField(max_length=20)
    phone_number= forms.IntegerField()