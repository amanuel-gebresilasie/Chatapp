from django.db import models

class Msg(models.Model):
    name = models.TextField()
    date = models.TextField()
    msg = models.TextField()
