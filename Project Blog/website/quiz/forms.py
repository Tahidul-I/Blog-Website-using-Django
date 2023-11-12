from quiz.models import make_quiz,Demoquiz
from django import forms

class QuizForm(forms.ModelForm):

    class Meta:
        model = Demoquiz
        firlds = '__all__'
        exclude = ('quiz_maker',)

