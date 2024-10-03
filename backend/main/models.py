from django.db import models

# Create your models here.

class Apple(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    photo_url = models.URLField()

    def __str__(self):
        return self.name
    
# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

#     def __str__(self):
#         return self.name