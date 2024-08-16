# restricted/models.py
# restricted/models.py
from django.db import models

class RestrictedPage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
