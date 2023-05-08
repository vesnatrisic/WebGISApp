from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    groups = models.ManyToManyField(
            'auth.Group',
            related_name='custom_user_groups',  # change related name to 'custom_user_groups'
            blank=True,
            help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
        )

    user_permissions = models.ManyToManyField(
            'auth.Permission',
            related_name='custom_user_permissions',  # change related name to 'custom_user_permissions'
            blank=True,
            help_text='Specific permissions for this user.'
        )
