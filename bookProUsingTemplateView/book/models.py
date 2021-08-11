from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=120)
    price=models.IntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=50)
    pages=models.IntegerField()

    def __str__(self):
        return self.name