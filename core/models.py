from django.db import models
from resources.models import Resource
from comments.models import Comment
from avaliations.models import Avaliation
from addresses.models import Address


class TuristicPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    resources = models.ManyToManyField(Resource)
    comments = models.ManyToManyField(Comment)
    avaliations = models.ManyToManyField(Avaliation)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="turistic_points", null=True, blank=True)

    def __str__(self):
        return self.name
