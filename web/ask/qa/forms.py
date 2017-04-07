from django.db import models
from django.contrib.auth.models import User
from django import forms
from qa.models import *
from django.contrib.auth import authenticate, login

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=200)##??
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    def save(self):
        user= User.objects.create_user(**self.cleaned_data)
        user.save()
        return user
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)##??
    password=forms.CharField(widget=forms.PasswordInput())            
        

class AskForm(forms.Form):
    title = forms.CharField(max_length=200)
    text =  forms.CharField(widget=forms.Textarea())
    def clean(self):
        pass      
    #def __init__(self,*args,**kwargs):    
     #   try:
      #      self.author = User.objects.get(id = kwargs.pop("user_id",1))
      #  except User.DoesNotExist:
        #    self.author = User.objects.get(id = 1)
       # super(AskForm,self).__init__(*args,**kwargs) 
   
    def save(self,user):
        question = Question(**self.cleaned_data,author=user)
        question.save()
        return question



class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
    question = forms.IntegerField(widget=forms.HiddenInput())    
    def clean(self):
        pass
    def save(self,useros,question):
        self.cleaned_data['author'] = useros
        self.cleaned_data['question']=question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
        
   
