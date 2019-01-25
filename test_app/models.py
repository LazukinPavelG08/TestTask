from django.db import models


class Profile(models.Model):
    vk_id = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    access_token = models.TextField()