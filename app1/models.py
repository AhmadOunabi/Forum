from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=264)
    author = models.CharField(max_length=264)
    question=models.CharField(max_length=5000)
    createDate = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    

class Answer(models.Model):
    question=models.ForeignKey(Question,related_name='question_answer',on_delete=models.CASCADE)
    author=models.CharField(max_length=264)
    answer=models.CharField(max_length=264)
    createDate=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.author