from django.db import models

# Create your models here.
class student(models.Model):
 
    name=models.CharField(max_length=20)
    age=models.IntegerField()

    def _str_(self):
        return self.name+" "+str(self.age)
    
class game(models.Model):
    name=models.CharField(max_length=30)             #instance var
    description=models.TextField(max_length=100)      #instance var

    def _str_(self):
        return self.name+" "+str(self.description)
