from django.db import models
from django.contrib.auth.models import User
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    # receipe_image = models.ImageField(upload_to='products/%Y/%m/%d/', height_field='image_height', width_field='image_width')
    receipe_view_count = models.PositiveIntegerField(default=1)