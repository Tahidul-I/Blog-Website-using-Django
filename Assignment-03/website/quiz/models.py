from django.db import models
from blog.models import User
from django.urls import reverse

# Create your models here.
class quiz_category(models.Model):
    under_whom = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    category = models.CharField(max_length=250,unique=True, blank=True,null=True)
    marks = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.category
    
# '''I have two models here which perform the same operatons that is making a quiz. I used 
# the "make_quiz" model for saving data using function based view which name is "question_save"
# function and the "Demoquiz" model for saving data by using class Based Visew which is 
# "CreateQuiz"  '''

class make_quiz(models.Model):
    quiz_type = models.ForeignKey(quiz_category,on_delete=models.CASCADE,related_name='quiz_category',unique=False)
    quiz_maker = models.ForeignKey(User,on_delete=models.CASCADE,related_name='quiz_maker')
    question = models.CharField(max_length=250, blank=True,null=True)
    option_1 = models.CharField(max_length=250, blank=True,null=True)
    option_2 = models.CharField(max_length=250, blank=True,null=True)
    option_3 = models.CharField(max_length=250, blank=True,null=True)
    option_4 = models.CharField(max_length=250, blank=True,null=True)
    answer = models.CharField(max_length=250, blank=True,null=True)

    def get_absolute_url(self):
        return reverse( 'edit_quiz')

class Demoquiz(models.Model):
    CHOICES = (
        ('option-1','option-1'),
        ('option-2','option-2'),
        ('option-3','option-3'),
        ('option-4','option-4')

    )
    quiz_type = models.ForeignKey(quiz_category,on_delete=models.CASCADE,related_name='quiz_type',unique=False)
    quiz_maker = models.ForeignKey(User,on_delete=models.CASCADE,related_name='quizer')
    question = models.CharField(max_length=250, blank=True,null=True)
    option_1 = models.CharField(max_length=250, blank=True,null=True)
    option_2 = models.CharField(max_length=250, blank=True,null=True)
    option_3 = models.CharField(max_length=250, blank=True,null=True)
    option_4 = models.CharField(max_length=250, blank=True,null=True)
    answer = models.CharField(max_length=250,choices=CHOICES,default='Select answer',  blank=True,null=True)

class student_score (models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    ques_category = models.ForeignKey(quiz_category, on_delete=models.CASCADE)
    score = models.CharField(max_length=500, blank=True,null=True)
    total_quiz_score = models.CharField(max_length=500,blank=True,null=True)
    

    
