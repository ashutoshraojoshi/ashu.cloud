# location_mapper/forms.py

from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['custom_name', 'google_maps_url']
