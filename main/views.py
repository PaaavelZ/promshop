from django.shortcuts import render
from django.views import View

from main.form import MessagesForm


class MainPage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': MessagesForm(),
        }
        return render(request, 'test/test.html', context)
    

class Test(View):
    def post(self, request, *args, **kwargs):
        form = MessagesForm(request.POST, request.FILES)
        context = {
            'form': MessagesForm(),
        }
        if form.is_valid():
            return render(request, 'test/aaa.html')
        else:
            return render(request, 'test/test.html', context)
