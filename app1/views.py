from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Question , Answer
from app1.forms import QuestionForm
# Create your views here.
def index(request):
    questions_list= Question.objects.all()
    answers_list= Answer.objects.all()
    my_dict= {"answers":answers_list,"questions":questions_list}
    return render(request,'page.html',context=my_dict)

def add(request):
    if request.method=="POST":
        QuestionForm(request.POST)
        if QuestionForm(request.POST).is_valid():
            QuestionForm(request.POST).save()
    else:
        QuestionForm()
    question_dict = {'question':QuestionForm}
    return render(request,'add.html',question_dict)
