from django.db import models

# Create your models here.


class Branch(models.Model):
    branch_name = models.CharField(max_length=200)
    branch_location = models.CharField(max_length=200)
    def __str__(self):
        return (f"Name: {self.branch_name} | Location: {self.branch_location}")