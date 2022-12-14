from django.db import models

class Contacts(models.Model):

    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()


class Comments(models.Model):

    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    comment = models.TextField()