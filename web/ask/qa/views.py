from django.shortcuts import render
from django.http import HttpResponse
from qa.models import *
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator, InvalidPage,EmptyPage
def test (request):
    return HttpResponse('OK')
    
    
def undoQuestion(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404
    answers = Question.objects.getAnswers(question)    
    return render(request,"q.html",{"question":question,"answers":answers})  
    

def displayPopularQuestion(request):

    page = request.GET.get('page',1)
    paginator= Paginator(Question.objects.popular(),10)
    paginator.baseurl ="/popular/?page="
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)    
    return render(request,"popular.html",{
        'questions':page.object_list,
        'paginator':paginator,
        'page':page,
    })    
    
def displayNewQuestion(request):
    page = request.GET.get('page',1)
    paginator= Paginator(Question.objects.new(),10)
    paginator.baseurl ="/?page="
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request,"new.html",{
        'questions':page.object_list,
        'paginator':paginator,
        'page':page,
    })    
                  





# Create your views here.
