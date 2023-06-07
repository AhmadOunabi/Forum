from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Question , Answer
from app1.forms import QuestionForm,AnswerForm
# Create your views here.
def index(request):
    questions_list= Question.objects.all()
    answers_list= Answer.objects.all()
    my_dict= {"answers":answers_list,"questions":questions_list}
    return render(request,'page.html',context=my_dict)

def add(request):
    if request.method=="POST":
        QuestionForm(request.POST)
        AnswerForm(request.POST)
        if QuestionForm(request.POST).is_valid() and AnswerForm(request.POST).is_valid():
            QuestionForm(request.POST).save()
            AnswerForm(request.POST).save()
    else:
        QuestionForm()
        AnswerForm()
    question_dict = {'question':QuestionForm, 'answer':AnswerForm}
    return render(request,'add.html',question_dict)

# def add_answer(request):
#     if request.method=="POST":
#         AnswerForm(request.POST)
#         if AnswerForm(request.POST).is_valid():
#             QuestionForm(request.POST).save()
#     else:
#         AnswerForm()
#     answer_dict={'answer':AnswerForm}
#     return render(request,'add.html',answer_dict)