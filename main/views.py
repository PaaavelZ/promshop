from django.shortcuts import render, redirect
from django.views import View

from main.form import MessagesForm
from main.helpers import GetContext

from mailing.mail import Mail
from dbcore.models import Feedback



class MainPage(View):
    def get(self, request, *args, **kwargs):
        context = GetContext(lang=kwargs.get('lang'))()
        context['form'] = MessagesForm()
        return render(request, 'main.html', context)
    

class Test(View):
    def post(self, request, *args, **kwargs):
        form = MessagesForm(request.POST, request.FILES)
        if form.is_valid():
            fio = form.cleaned_data.get('fio')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('comment')

            feedback = Feedback(
                fio=fio,
                phone=phone,
                email=email,
                text=text
            )
            feedback.save()

            Mail(feedback)()

        return redirect('main:main_page', lang=kwargs.get('lang'))

        
