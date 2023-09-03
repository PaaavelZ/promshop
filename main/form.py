from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
 

class ContactField(forms.Field):
    def validate(self, value):
        super().validate(value)
        if 'aa' not in value:
            raise ValidationError(("Invalid value:"))
        

 
class MessagesForm(forms.Form):
    fio = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={
                                'type': 'text',
                                'name': 'fio',
                                'class': 'input-field form_fio',
                                'id': 'id_fio',
                                'placeholder': 'ФИО'})
                          )
    phone = forms.CharField(empty_value='',
                            required=False,
                            widget=forms.TextInput(attrs={
                                'type': 'tel',
                                'name': 'tel',
                                'class': 'input-field form_tel',
                                'id': 'id_fio',
                                'placeholder': 'ТЕЛЕФОН'})
                            )
    email = forms.CharField(widget=forms.TextInput(attrs={
                                 'type': 'email',
                                 'name': 'email',
                                 'class': 'input-field form_mail',
                                 'id': 'id_fio',
                                 'placeholder': 'EMAIL'})
                         )
    comment = forms.CharField(widget=forms.TextInput(attrs={
                                'type': 'text',
                                'name': 'info',
                                'class': 'input-field form_info',
                                'id': 'id_fio',
                                'placeholder': 'СООБЩЕНИЕ'})
                          )
    
