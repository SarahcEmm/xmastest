from django.contrib.auth.models import User
from django.db import models

class ChristmasList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    visibility = models.CharField(
        max_length=10,
        choices=[('public', 'Public'), ('private', 'Private')],
        default='private'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GiftItem(models.Model):
    christmas_list = models.ForeignKey(ChristmasList, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)  # Option to add a link to the gift
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.name