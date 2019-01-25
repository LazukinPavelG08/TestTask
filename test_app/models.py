from django.db import models


class Profile(models.Model):
    vk_id = models.CharField(max_length=200)
    first_name = models.TextField()
    last_name = models.TextField()
    access_token = models.TextField()