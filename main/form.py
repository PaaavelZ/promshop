from dataclasses import dataclass
from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
 

class ContactField(forms.Field):
    def validate(self, value):
        super().validate(value)
        if 'aa' not in value:
            raise ValidationError(("Invalid value:"))
        

@dataclass
class GetPlaceholder:
    lang: str
    dct_lang = {
        'ru': {
            'fio': '    ФИО',
            'phone': '    ТЕЛЕФОН',
            'email': '    EMAIL',
            'comment': '    СООБЩЕНИЕ'
        },
        'eng': {
            'fio': '    FULL NAME',
            'phone': '    PHONE',
            'email': '    EMAIL',
            'comment': '    MESSAGE'
        },
        'kz': {
            'fio': '    ТАӘ',
            'phone': '    ТЕЛЕФОН',
            'email': '    EMAIL',
            'comment': '    ХАБАР'
        }
    }

    def __call__(self, placeholder: str) -> str:
        if self.lang not in ('ru', 'kz', 'eng'):
            self.lang = 'kz'

        return self.dct_lang[self.lang].get(placeholder)
        

class MessagesForm(forms.Form):

    fio = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={
                                'type': 'text',
                                'name': 'fio',
                                'class': 'input-field form_fio',
                                'id': 'id_fio',})
                          )
    phone = forms.CharField(empty_value='',
                            required=False,
                            widget=forms.TextInput(attrs={
                                'type': 'tel',
                                'name': 'tel',
                                'class': 'input-field form_tel',
                                'id': 'id_fio',})
                            )
    email = forms.CharField(widget=forms.TextInput(attrs={
                                 'type': 'email',
                                 'name': 'email',
                                 'class': 'input-field form_mail',
                                 'id': 'id_fio',})
                         )
    comment = forms.CharField(widget=forms.TextInput(attrs={
                                'type': 'text',
                                'name': 'info',
                                'class': 'input-field form_info',
                                'id': 'id_fio',})
                          )

    def __init__(self, *args, **kwargs) -> None:
        lang = kwargs.pop('lang', None)
        super(MessagesForm, self).__init__(*args, **kwargs)

        self.fields['fio'].widget.attrs['placeholder'] = GetPlaceholder(lang=lang)(placeholder='fio')
        self.fields['phone'].widget.attrs['placeholder'] = GetPlaceholder(lang=lang)(placeholder='phone')
        self.fields['email'].widget.attrs['placeholder'] = GetPlaceholder(lang=lang)(placeholder='email')
        self.fields['comment'].widget.attrs['placeholder'] = GetPlaceholder(lang=lang)(placeholder='comment')
  
