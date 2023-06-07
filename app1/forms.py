from django import forms
from app1.models import Question,Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields= '__all__'