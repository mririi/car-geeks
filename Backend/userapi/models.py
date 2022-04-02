from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "This is the link to reset your password http://localhost:8080/api/password_reset_confirm/?token={}".format(reset_password_token.key)

    send_mail(
        # title:
        "Password Reset {title}".format(title="Car Geeks"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@cargeeks.local",
        # to:
        [reset_password_token.user.email]
    )