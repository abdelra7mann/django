from django.db import models

class Member(models.Model):
    fName = models.CharField(max_length=250)
    lastNmae = models.CharField(max_length=255)
    # email = models.EmailField()