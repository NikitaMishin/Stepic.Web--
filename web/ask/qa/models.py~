from django.db import models
from django.contrib.auth.models import User
class QuestionManager(models.Manager):
    def new(self):
        return self.objects.order_by('-added_at')
    def popular(self):
        return   self.objects.order_by('-raiting')      

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=200,unique = True,verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    added_at = models.DateTimeField(auto_now_add=True,verbose_name="time_of_adding")
    raiting = models.IntegerField(verbose_name = "raiting",default = 0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User,related_name ='question_like_user')
    
class Answer(models.Model):
    text = models.TextField(verbose_name="Text")
    added_at = models.DateTimeField(auto_now_add = True,verbose_name="time_of_adding")
    question = models.ForeignKey(Question)
    author =  models.ForeignKey(User)
    

