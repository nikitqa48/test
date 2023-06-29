from django.db import models
from django.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=2000)
    director = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='company', null=True)

    class Meta:
        unique_together = ('name', 'director')

    def __str__(self):
        return self.name
