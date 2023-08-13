from django.db import models

# Create your models here.
class Dept(models.Model):
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
