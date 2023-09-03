from django.shortcuts import render
from django.views import View

from main.form import MessagesForm
from main.helpers import GetContext


class MainPage(View):
    def get(self, request, *args, **kwargs):
        context = GetContext(lang=kwargs.get('lang'))()
        context['form'] = MessagesForm()
        return render(request, 'main.html', context)
    

class Test(View):
    def post(self, request, *args, **kwargs):
        form = MessagesForm(request.POST, request.FILES)
        context = {
            'form': MessagesForm(),
        }

        
