from django.urls import path

from main.views import MainPage, Test


app_name = 'main'


urlpatterns = [
    path('<str:lang>/', MainPage.as_view(), name='main_page'),
    path('feedback/', Test.as_view(), name='feedback'),
]