from django.shortcuts import render,redirect
from blog.models import User,account
from quiz.models import quiz_category,make_quiz,Demoquiz,student_score
from quiz.forms import QuizForm
import sweetify
from django.views.generic import CreateView,UpdateView
from django.db import models
# Create your views here.
def create_quiz(request):
    

    return render(request,'quiz/quiz.html')
def make_question(request):

    try:
         quiz_type = quiz_category.objects.filter( under_whom_id = request.user.id )
         status = True
         context={
            'quiz_type':quiz_type,
            'status':status
            }
            
        
           
         return render(request,'quiz/make_question.html',context)
           
    
    except:
        
        return render(request,'quiz/make_question.html')    


def set_category(request):
    if request.method == 'POST':
        category = request.POST.get('title')
        marks = request.POST.get('mark')
        data = quiz_category(
           category = category,
            marks = marks,
            under_whom = request.user
        )
        data.save()
        return redirect('create_quiz')

    return render(request,'quiz/set_category.html')

# '''I have two models here which perform the same operatons that is making a quiz. I used 
# the "make_quiz" model for saving data using function based view which name is "question_save" function
#  and the "Demoquiz" model for saving data by using class Based Visew which is 
# "CreateQuiz". But for this project, I used the function based views but the class based 
# view just works fine  '''

def question_save(request):
     if request.method=='POST':
            
            type = request.POST.get('title')
            question = request.POST.get('question')
            option_1 = request.POST.get('option_1')
            option_2 = request.POST.get('option_2')
            option_3 = request.POST.get('option_3')
            option_4 = request.POST.get('option_4')
            answer = request.POST.get('answer')
            
            
            if answer == 'option-1':
                correct_answer = option_1
                print('number1')
            elif answer == 'option-2':
                correct_answer = option_2
            elif answer == 'option-3':
                correct_answer = option_3
            else:
                correct_answer = option_4
            
            cate_gory = quiz_category.objects.get(category=type)
            

            data = make_quiz(
                quiz_type = cate_gory,
                quiz_maker = request.user,
                question = question,
                option_1 = option_1,
                option_2 = option_2,
                option_3 = option_3,
                option_4 = option_4,
                answer = correct_answer


            )
            data.save()
            sweetify.success(request, 'Question added successfully')
            return redirect('create_quiz')

            
     

def take_quiz(request):
    if request.method=="POST":
        option = request.POST.get('django')
        option2 = request.POST.get('django2')
        print(option)
        print(option2)
        return redirect('create_quiz')
    
    return render(request,'quiz/take_quiz.html')

# '''I have two models here which perform the same operatons that is making a quiz. I used 
# the "make_quiz" model for saving data using function based view which name is "question_save" function
#  and the "Demoquiz" model for saving data by using class Based Visew which is 
# "CreateQuiz". But for this project, I used the function based views but the class based 
# view just works fine Use the required link in the base.html nav link named Make quiz '''

class CreateQuiz(CreateView):
    
    model = Demoquiz
    form_class = QuizForm
    template_name = 'quiz/demo.html'
    
    def form_valid(self,form):
        quiz_obj = form.save(commit=False)
        quiz_obj.quiz_maker = self.request.user
        correct_answer = quiz_obj.answer
        
        if quiz_obj.answer == 'option-1':
                correct_answer = quiz_obj.option_1
                quiz_obj.answer = correct_answer  
                quiz_obj.save()
                return redirect('create_quiz')
        elif quiz_obj.answer == 'option-2':
                correct_answer = quiz_obj.option_2
                quiz_obj.answer = correct_answer
                quiz_obj.save()
                return redirect('create_quiz')
        elif quiz_obj.answer == 'option-3':
                correct_answer = quiz_obj.option_3
                quiz_obj.answer = correct_answer
                quiz_obj.save()
                return redirect('create_quiz')
        else:
                correct_answer = quiz_obj.option_4
                quiz_obj.answer = correct_answer
                quiz_obj.save()
                return redirect('create_quiz')


def edit_quiz(request):
        quiz_section  = quiz_category.objects.filter( under_whom_id = request.user.id ).all()

        if quiz_section.exists():
             status = True
             
             context = {
                  'quiz_section' :quiz_section ,
                  'status' : status
             }
             return render(request,'quiz/edit_quiz.html',context)   
        else: 
             status = False
             context = {
                  'status':status
             } 
             return render(request,'quiz/edit_quiz.html',context)

        
def edit_quiz_question(request,pk):
    
        questions = make_quiz.objects.filter(quiz_type_id = pk).all()
        status = True
        context = {
        'questions':questions,
        'status':status
        }
        return render(request,'quiz/edit_question.html',context)
    
          
     


class UpdateQuiz(UpdateView):
     model = make_quiz
     fields = ('question','option_1','option_2','option_3','option_4','answer')
     context_object_name = 'data'
     template_name = 'quiz/update_quiz.html'

def student_quiz(request):
     acc_data = account.objects.get( type = 'Teacher' )
     teacher_data = User.objects.filter(user_type=acc_data.id)
     context = {
          'teacher_data':teacher_data
     }
     return render(request,'quiz/teacher_table.html',context)
def select_quiz_category(request,id):
     teacher = User.objects.get(id=id)
     quiz_cat = quiz_category.objects.filter(under_whom = teacher)
     checker =quiz_cat.first() 
     if checker:
          
          
          status = True
          context = {
               'quiz_cat':quiz_cat,
               'status':status
          }

          return render(request,'quiz/select_quiz.html',context)
     else:
          status = False
          context={
               'status':status
          }
          return render(request,'quiz/select_quiz.html',context)

def exam_quiz(request,id):
     category = quiz_category.objects.get(id = id)
     checker = student_score.objects.filter(ques_category = category )
     question_data = make_quiz.objects.filter( quiz_type =category )


     context={
          'question_data':question_data,
          'category':category,
          'checker':checker
     }

     if request.method=='POST':
          print("I am in the POST block ")
          ques_ans_1 = request.POST.get('question_12')
          ques_ans_2 = request.POST.get('question_13')
          ques_ans_3 = request.POST.get('question_14')
          print(ques_ans_1)
          print(ques_ans_2)
          print(ques_ans_3)
          total_marks = 0
          out_of = 0
          for i in question_data:
               ques_answer = request.POST.get(f"question_{i.id}")
               print(i.id)
               print(ques_answer)
               out_of +=category.marks
               if i.answer == ques_answer:
                    total_marks+=category.marks
                    print("Correct answer")
               
          

          stu_score = student_score(
               student = request.user,
               ques_category = category,
               score = total_marks,
               total_quiz_score = out_of

          )
          stu_score.save()
          sweetify.info(request,"Check score in your result section")
          return redirect ('student_quiz')       
     return render(request,'quiz/take_quiz.html',context)

def score_card(request):
     score_details = student_score.objects.filter(student=request.user)
     context = {
          'score_details':score_details
     }

     return render(request,'quiz/score_card.html',context)
          
     

     
                
        
        
