from pickle import TRUE
from django.db import models


# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    comment = models.TextField()
    retrievetime = models.DateTimeField(auto_now_add=TRUE)
    abstract = models.TextField()
    publishTime = models.DateTimeField()
    area = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    class Meta:
        db_table = "Paper"

    def __str__(self):
        return self.title


class Keywords(models.Model):
    content = models.CharField(max_length=50)
    paper = models.ManyToManyField('Paper',related_name='keywords')
    class Meta:
        db_table = "Keywords"

    def __str__(self):
        return self.name
