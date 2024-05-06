# services.py

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.core.mail import send_mail
from django.urls import reverse

def register_user(email, password):
    User = get_user_model()
    user = User.objects.create_user(email=email, password=password)
    user.save()

def authenticate_user(email, password):
    User = get_user_model()
    user = User.objects.filter(email=email).first()
    if user and user.check_password(password):
        return user
    return None

def send_password_reset_email(email):
    User = get_user_model()
    user = User.objects.filter(email=email).first()
    if user:
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_str(user.pk).encode())
        reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
        reset_url = f"http://yourdomain.com{reset_url}"
        message = f"Click the following link to reset your password: {reset_url}"
        send_mail('Password Reset', message, 'from@example.com', [email])

def reset_password(uidb64, token, new_password):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.set_password(new_password)
        user.save()
        return user
    return None
