from django.urls import path

from main.views import MainPage, Page, Feedback


app_name = 'main'


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('<str:lang>/', Page.as_view(), name='main_page'),
    path('<str:lang>/feedback/', Feedback.as_view(), name='feedback'),
]