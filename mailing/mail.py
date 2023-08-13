from django.core.mail import send_mail

from dataclasses import dataclass
from typing import Any

from aaps.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from dbcore.models import FeedbackEmailEntry


@dataclass
class Mail:
    subject: str
    text: str
    email_inst: FeedbackEmailEntry or None
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self._try_to_send():
            self._create_email_entry()
            self._mark_as_sent()

        return 
    
    def _try_to_send(self) -> bool:
        try:
            send_mail('+1 к новым смс', 
                      'Новое сообщение!',
                      DEFAULT_FROM_EMAIL, 
                      RECIPIENTS_EMAIL)
        except:
            return False
        
        return True
    
    def _create_email_entry(self) -> None:
        self.email_inst = FeedbackEmailEntry.objects.create(
            feedback=self.feedback
        )

    def _mark_as_sent(self) -> None:
        self.email_inst.send = True
        self.email_inst.save()
