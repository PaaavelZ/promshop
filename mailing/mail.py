import smtplib, ssl

from dataclasses import dataclass
from typing import Any

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from aaps.settings import RECIPIENTS_EMAIL, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from dbcore.models import Feedback, EmailEntry


@dataclass
class Mail:
    feedback: Feedback
    em: str = ''
    text: str = ''

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self._prepare_sms()
        self._send()
        self._mark_as_sent()

    def _prepare_sms(self):
        e = MIMEMultipart()
        e['From'] = EMAIL_HOST_USER
        e['To'] = ', '.join(RECIPIENTS_EMAIL)
        e['Subject'] = 'Новое сообщение'

        self.text = f'ФИО: {self.feedback.fio} \nТЕЛЕФОН: {self.feedback.phone} \nПОЧТА: {self.feedback.email} \nСООБЩЕНИЕ: {self.feedback.text}'
        e.attach(MIMEText(self.text, 'plain'))
        self.em = e.as_string()

    def _send(self):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(
                EMAIL_HOST_USER, 
                EMAIL_HOST_PASSWORD,
            )
            server.sendmail(EMAIL_HOST_USER, RECIPIENTS_EMAIL, self.em)

    def _mark_as_sent(self):
       EmailEntry.objects.create(
           feedback=self.feedback,
           subject = 'Новая заявка',
           text = self.text,
           is_sent=True
       )

    
