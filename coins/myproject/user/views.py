from sqlite3 import IntegrityError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, permissions,  status
from rest_framework.authtoken.models import Token
from .services import authenticate_user
from .serializers import *
from django.core.mail import send_mail
from django.conf import settings
from django.db import IntegrityError
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.permissions import IsAuthenticated
User = get_user_model()

class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer  # Указываем класс сериализатора

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # email = serializer.validated_data['email']
            email = str(serializer.validated_data['email'])

            first_password = serializer.validated_data['first_password']
            last_password = serializer.validated_data['last_password']

            # Проверяем, существует ли пользователь с предоставленным адресом электронной почты
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Электронный адрес уже существует'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = serializer.save()
                user.set_password(first_password)  # Сохраняем пароль
                user.save()  # Сохраняем пользователя в базу данных

                # Отправляем электронное письмо для активации
                subject = 'Активация аккаунта'
                message = f'Здравствуйте, {email}!\n\nПоздравляем Вас с успешной регистрацией на сайте {settings.BASE_URL}\n\nВаш пароль: {first_password}\n\n  {settings.BASE_URL} Активация аккаунта \n\nС наилучшими пожеланиями,\nКоманда {settings.BASE_URL}\n\nДля активации вашего аккаунта перейдите по ссылке: {settings.BASE_URL}'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [user.email]

                send_mail(subject, message, from_email, recipient_list)

                # Входим пользователя после регистрации
                authenticated_user = authenticate(email=email, password=first_password)
                login(request, authenticated_user)

                # Добавляем кнопку на главную страницу
                homepage_url = "/"  # Замените эту строку на реальный URL вашей главной страницы
                # return '{"response": True, "message": "Пользователь успешно зарегистрирован. Проверьте вашу электронную почту для получения инструкций по активации.", "homepage_url": "/"}'

                return Response({'response': True, 'message': 'Пользователь успешно зарегистрирован. Проверьте вашу электронную почту для получения инструкций по активации.', 'homepage_url': '/'}, status=status.HTTP_201_CREATED)


            except IntegrityError:
                return Response({'error': 'Произошла ошибка при регистрации пользователя'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'response': False, 'message': 'Ошибка при регистрации пользователя'}, status=status.HTTP_400_BAD_REQUEST)




class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [IsAuthenticated]  # Требуется аутентификация

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate_user(serializer.validated_data['email'], serializer.validated_data['password'])
        if user:
            return Response({'response': True}, status=status.HTTP_200_OK)
        else:
            return Response({'response': True,'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfileListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  

    def get(self, request, *args, **kwargs):
        profiles = self.queryset.all()
        serializer = self.serializer_class(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ResetPasswordView(GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                # Отправить электронное письмо с данными для сброса пароля
                # (необходимо добавить эту логику)
                return Response({'message': 'Запрос на сброс пароля успешно отправлен.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Запрос на сброс пароля успешно отправлен.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordVerifyView(GenericAPIView):
    serializer_class = ResetPasswordVerifySerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data.get('token')
            new_password = serializer.validated_data.get('new_password')

            try:
                uid = force_text(urlsafe_base64_decode(token))
                user = User.objects.get(pk=uid)

                if default_token_generator.check_token(user, token):
                    user.set_password(new_password)
                    user.save()
                    return Response({'message': 'Пароль успешно сброшен.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Неверный токен для сброса пароля.'}, status=status.HTTP_400_BAD_REQUEST)
            except (TypeError, ValueError, OverflowError, ObjectDoesNotExist):
                return Response({'message': 'Неверный токен для сброса пароля.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
