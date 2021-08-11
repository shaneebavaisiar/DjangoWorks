from django.db import models
import os
from twilio.rest import Client

# Create your models here.
class Score(models.Model):
    result=models.PositiveIntegerField()
    def __str__(self):
        return str(self.result)

    def save(self,*args,**kwargs):
        if self.result<70:
            account_sid = 'AC17948d4503e49067e302cd12f0ea34ce'
            auth_token = '78f7ce4ab44156220b43b866da026173'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'the current result is bad-{self.result}',
                from_='(608) 728-7240',
                to='+91 9562013782'
            )

            print(message.sid)
        return super().save(*args,**kwargs)