from django.core.mail import send_mail  

send_mail(
            'subject', 
            'body of the message', 
            'sender@example.com', 
            [
                'receiver1@example.com', 
                'receiver2@example.com'
            ]
        ) 
