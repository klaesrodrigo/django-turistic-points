from django.db import models


class Resource(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    work_hour = models.TextField()
    min_age = models.IntegerField()

    def __str__(self):
        return self.name
