from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TIME = [('長時間', '長時間'), ('普通', '普通'),('短時間', '短時間')]
class ReviewModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    useful_review = models.IntegerField(null=True, blank=True, default=0)
    useful_review_record = models.TextField()
    evaluation = models.CharField(max_length=10, choices=TIME)
