from django import forms
from django.core.exceptions import ValidationError
 

class ContactField(forms.Field):
    def validate(self, value):
        super().validate(value)
        if 'aa' not in value:
            raise forms.ValidationError(("Invalid value:"))
        

 
class MessagesForm(forms.Form):
    contact = ContactField(required=True,)
