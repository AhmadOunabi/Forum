from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import Question , Answer
from app1.forms import QuestionForm,AnswerForm
# Create your views here.
def index(request):
    questions_list= Question.objects.all()
    return render(request,'page.html',{"questions":questions_list})

def add_question(request):
    if request.method=="POST":
        QuestionForm(request.POST)
        if QuestionForm(request.POST).is_valid():
            QuestionForm(request.POST).save()
    else:
        QuestionForm()
    question_dict = {'question':QuestionForm}
    return render(request,'add_question.html',question_dict)

def details(request,id):
    question=Question.objects.get(id=id)
    answers= Answer.objects.filter(question=question)
    return render(request,'details.html',{'question':question,'answers':answers})