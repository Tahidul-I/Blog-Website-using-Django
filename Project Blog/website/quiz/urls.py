from django.urls import path 
from quiz import views
urlpatterns=[
    path('create_quiz/',views.create_quiz, name='create_quiz'),
    path('take_quiz/',views.take_quiz, name='take_quiz'),
    path('set_category/',views.set_category, name='set_category'),
    path('make_question/',views.make_question, name='make_question'),
    path('question_save/',views.question_save, name='question_save'),
    path('write/',views.CreateQuiz.as_view(), name='CreateQuiz'),
    path('edit_quiz/',views.edit_quiz, name='edit_quiz'),
    path('edit_quiz_question<pk>/',views.edit_quiz_question, name='edit_quiz_question'),
    path('UpdateQuiz<pk>/',views.UpdateQuiz.as_view(), name='UpdateQuiz'),
    path('student_quiz/',views.student_quiz, name='student_quiz'),
    path('select_quiz_category/<int:id>',views.select_quiz_category, name='select_quiz_category'),
    path('exam_quiz/<int:id>',views.exam_quiz, name='exam_quiz'),
    path('score_card/',views.score_card, name='score_card'),
]