"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.

# The project includes a nearly empty file called things/forms.py. In this file, define a form called ThingForm, that contains the fields name, description, and quantity, but not created_at.
#The form must accept valid inputs for Thing and reject invalid input for Thing.
# The description field must be displayed as a Textarea. The quantity field must be displayed as NumberInput.

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea,
            'quantity': forms.NumberInput
        }