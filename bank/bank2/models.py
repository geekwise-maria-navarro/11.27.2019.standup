from django.db import models

# Create your models here.


class Branch(models.Model):
    branch_name = models.CharField(max_length=200)
    branch_location = models.CharField(max_length=200)
    def __str__(self):
        return (f"Name: {self.branch_name} | Location: {self.branch_location}")


class Customer(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
    )
    
    customer_name = models.CharField(max_length=300)
    customer_email = models.EmailField(max_length=300)
    def __str__(self):
        return (f"Name: {self.customer_name} | Email: {self.customer_email} | Bank: {self.branch.branch_name}")