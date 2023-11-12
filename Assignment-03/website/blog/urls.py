from django.urls import path
from blog import views
urlpatterns=[
    path('',views.home, name='home'),
    path('user_signup/',views.user_signup, name='user_signup'),
    path('user_login/',views.user_login, name='user_login'),
    path('user_logout/',views.user_logout, name='user_logout'),
    path('user_profile/',views.user_profile, name='user_profile'),
    path('create_profile/',views.create_profile, name='create_profile'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('search/',views.search, name='search'),
    
]