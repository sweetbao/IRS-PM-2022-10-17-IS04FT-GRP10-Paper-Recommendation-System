from pickle import TRUE
from django.db import models

# Create your models here.
class UserPrefer(models.Model):
    Domain = models.TextField()
    Keywords = models.TextField()
    comment = models.TextField()
    UserID=models.IntegerField()
    retrievetime = models.DateTimeField( auto_now_add=TRUE)

    class Meta:
        db_table="UserPrefer"

    def __str__(self):
        return self.name
    
class UserViewRecord(models.Model):
    PaperId = models.IntegerField()
    UserID=models.IntegerField()
    retrievetime = models.DateTimeField( auto_now_add=TRUE)

    class Meta:
        db_table="UserViewRecord"

    def __str__(self):
        return self.name
