from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Question , Answer
# Create your views here.
def index(request):
    questions_list= Question.objects.all()
    answers_list= Answer.objects.all()
    my_dict= {"answers":answers_list,"questions":questions_list}
    return render(request,'page.html',context=my_dict)
