from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    matricule = models.CharField(max_length=255)
    pass
