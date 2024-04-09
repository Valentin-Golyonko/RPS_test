# from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


"""
# create 1M users:

from dj_core.models import CustomUser

objs = []
for count in range(0, 1_000_000):
    objs.append(CustomUser(username=f"user {count}"))

CustomUser.objects.bulk_create(objs=objs, batch_size=1_000)

CustomUser.objects.count()
"""
