from django.urls import path

from main.views import MainPage, Page, FeedbackView


app_name = 'main'


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('<str:lang>/', Page.as_view(), name='page_with_lang'),
    path('<str:lang>/feedback/', FeedbackView.as_view(), name='feedback'),
]