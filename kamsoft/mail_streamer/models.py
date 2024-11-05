# mail_streamer/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Добавьте дополнительные поля по мере необходимости
    pass
