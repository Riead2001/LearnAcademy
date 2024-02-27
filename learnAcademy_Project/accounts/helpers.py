

from django.core.mail import send_mail
from django.conf import settings
import traceback

def send_forget_password_mail(email, token):
    try:
        subject = 'Your forget password link'
        message = f'Hi, click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return True
    except Exception as e:
        print("Error sending email:", e)
        traceback.print_exc()  # Print traceback for detailed error information
        return False
