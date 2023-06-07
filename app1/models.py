from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=264)
    author = models.CharField(max_length=264)
    question=models.TextField()
    createDate = models.DateField()
    def __str__(self):
        return self.title
    

class Answer(models.Model):
    author=models.CharField(max_length=264)
    answer=models.CharField(max_length=264)
    createDate=models.DateField()
    def __str__(self):
        return self.author