import jwt
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from datetime import datetime, timedelta
from django.conf import settings
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,
                    first_name=None,
                    last_name=None,
                    username=None,
                    email=None,
                    role='MU',
                    password=None,
                    contact=None,
                    adress=None,
                    ):
        """
        create a user with the above fields
        """
        if not first_name:
            raise TypeError("First name is required.")

        if not last_name:
            raise TypeError("Last name is required.")

        if not email:
            raise TypeError("email name is required.")

        if not password:
            raise TypeError("password name is required.")

        if not contact:
            raise TypeError("contact name is required.")

        if not adress:
            raise TypeError("address name is required.")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            contact=contact,
            adress=adress
        )

        user.set_password(password)
        user.role = role
        user.is_verified = False
        user.save()
        return user

    def create_superuser(self,
                         first_name=None,
                         last_name=None,
                         username=None,
                         password=None,
                         email=None,
                         role='MU',
                         contact=None,
                         adress=None,
                         ):
        """
        create a user with the above fields
        """
        if not first_name:
            raise TypeError("First name is required.")

        if not last_name:
            raise TypeError("Last name is required.")

        if not email:
            raise TypeError("email name is required.")

        if not password:
            raise TypeError("password name is required.")

        if not contact:
            raise TypeError("contact name is required.")

        if not adress:
            raise TypeError("adress name is required.")

        user = self.model(first_name=first_name, last_name=last_name,
                          username=username, email=self.normalize_email(email), role='MA')
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_verified = True
        user.save()


class User(AbstractUser):
    USER_ROLES = (
        ('MA', 'MAX ADMIN'),
        ('MU', 'MAX USER'),
    )
    role = models.CharField(max_length=2, choices=USER_ROLES, default='MU')
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    adress = models.CharField(max_length=60)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'contact', 'adress', 'username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self.generate_jwt_token()

    def generate_jwt_token(self):
        token_expiry = datetime.now()+timedelta(hours=24)

        token = jwt.encode({
            'id': self.pk,
            'expiry': int(token_expiry.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf8')
