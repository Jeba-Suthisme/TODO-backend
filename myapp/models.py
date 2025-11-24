from django.db import models

# Create your models here.
# chocolate todo
class Chocolate(models.Model):
    chocolate_name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chocolate_name

# login 
class Register(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10,unique=True)
    email=models.EmailField()

    def _str_(self):
     return self.name   

# email
# class Contact(models.Model):
#     name=models.CharField(max_length=50)
#     phone_number=models.BigIntegerField()
#     email=models.EmailField()

#     def __str__(self):
#         return self.name     

