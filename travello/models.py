from django.db import models

# Create your models here.
# class Destination:
#     name : str
#     desc : str
#     price : int
#     img : str
#     offer : bool
# DESTINATION IS JUST A CLASS TO CONVERT INTO A MODEL WE HAVE TO INHERIT models.Model

class Destination(models.Model):
     name = models.CharField(max_length = 100)
     desc = models.TextField()
     price = models.IntegerField()
     img = models.ImageField(upload_to = 'pics')
     offer = models.BooleanField(default = False)

     def __str__(self):
          return self.name