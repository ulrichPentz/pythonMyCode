from django.db import models
from django.contrib.auth.models import User
class Demographics(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    demographics_name = models.CharField(max_length=100)
    demographics_surname = models.CharField(max_length=100)
    demographics_age = models.IntegerField()
    demographics_address = models.TextField()
    demographics_image = models.ImageField(upload_to ='uploads/')
    demographics_view_count = models.PositiveIntegerField(default=1)