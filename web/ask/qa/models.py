from django.db import models
from django.contrib.auth.models import User
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')##???
    def popular(self):
        return   self.get_queryset().order_by('-rating') 
    def getAnswers(self,question):
        return Answer.objects.filter(question=question)        

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=200,unique = True,verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    added_at = models.DateTimeField(auto_now_add=True,verbose_name="time_of_adding")
    rating = models.IntegerField(verbose_name = "raiting",default = 0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User,related_name ='question_like_user')
    
class Answer(models.Model):
    text = models.TextField(verbose_name="Text")
    added_at = models.DateTimeField(auto_now_add = True,verbose_name="time_of_adding")
    question = models.ForeignKey(Question)
    author =  models.ForeignKey(User)
    

