from django.urls import path

from main.views import MainPage, Page, FeedbackView, InvalidCaptchaToFeedback
from main.decorators import recaptcha


app_name = 'main'


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('<str:lang>/', Page.as_view(), name='page_with_lang'),
    path('<str:lang>/feedback/', recaptcha(FeedbackView.as_view()), name='feedback'),
    path('<str:lang>/invalid/', InvalidCaptchaToFeedback.as_view(), name='invalid_feedback'),
]