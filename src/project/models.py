from django.db import models
from src.personal.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=200)
    employments = models.ManyToManyField(CustomUser)
    lead = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='project_lead')
