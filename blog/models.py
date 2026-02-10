from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    likes = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.title
    

class Sample(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
    