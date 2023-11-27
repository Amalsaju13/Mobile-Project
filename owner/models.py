from django.db import models

# Create your models here.
class Mobiles(models.Model):
    brand=models.CharField(max_length=120)
    name=models.CharField(max_length=100)
    specification=models.CharField(max_length=200)
    ram=models.CharField(max_length=20)
    storage=models.CharField(max_length=20)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.name
