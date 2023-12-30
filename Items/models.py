from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.category


class Items(models.Model):
    identifier = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 200)
    price = models.PositiveIntegerField()
    # image = ArrayField((models.CharField(max_length = 100, default = "no_link")), size = 3, default = list)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # quantity = ArrayField((models.PositiveIntegerField(default = 0)), size = 5, default = list)

    
