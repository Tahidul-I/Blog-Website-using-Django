from django.shortcuts import render,redirect,get_object_or_404
from blog.models import User,account,account_confirmation
from main_blog.models import Creating_blog
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import sweetify
from blog.forms import ProfileForm
from blog.models import profile

# Create your views here.


def home(request):
    blog_data = Creating_blog.objects.all().order_by('-id')[0:10]
    context = {
        'blog_data':blog_data
    }
    return render(request,'blog/home.html',context)

def user_signup(request):
    account_type = account.objects.all()
    context = {
        'account_type':account_type
        
    }
    if request.method=='POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            acc_type = request.POST.get('account')
            code = request.POST.get('code')
            password = request.POST.get('pass1')
            confirm_password = request.POST.get('pass2')
            if password == confirm_password :
            
                if acc_type =='Teacher':
                
                    account_checker = account.objects.get(type =acc_type )
                    data = User(
                            username = username,
                            email = email,
                            password = make_password(password),
                            user_type = account_checker
                            )
                    data.save()
                    sweetify.success(request, 'You successfully created your account')
                    return redirect('user_login') 
                
                else:
                    
                    account_checker = account.objects.get(type =acc_type )
                    data = User(
                            username = username,
                            email = email,
                            password = make_password(password),
                            user_type = account_checker
                            )
                    data.save() 
                    sweetify.success(request, 'You successfully created your account')
                    return redirect('user_login')
                    
        except:
            sweetify.error(request, 'Username already taken ')
            return redirect('user_signup')

    return render(request,'blog/signup.html', context)


def user_login(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(username = username, password = password )

        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'blog/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def user_profile(request):

    try:
        status = True

        data = profile.objects.get(user_acc = request.user)
        context ={
        'data':data,
        'status':status
         } 
            
        return render(request,'blog/profile.html',context)
    except:
        status = False
        return render(request,'blog/profile.html')

    
        


   



def create_profile(request):
    form = ProfileForm()
    context={
        'form':form
    }

    if request.method=='POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            profile_pic = form.cleaned_data.get('profile_pic')
            print(first_name)
            print(last_name)

            data = profile(
                first_name = first_name,
                last_name = last_name,
                profile_pic = profile_pic,
                user_acc = request.user


            )
            data.save()
        
        return redirect('user_profile')

    return render(request,'blog/create_profile.html',context)

def edit_profile(request):

    current_user = profile.objects.get( user_acc = request.user )
    
    form = ProfileForm( instance =current_user )
    
    context = {
        'form':form
    }

    if request.method=='POST':
        data = ProfileForm(request.POST, request.FILES, instance = current_user)
        data.save()
        
        return redirect('user_profile')
    return render(request,'blog/edit_profile.html',context)


def search(request):
    if request.method=='GET':
        print("How it is done")
        text = request.GET.get("searched_text")
        blog_data = Creating_blog.objects.filter(blog_title__icontains=text)
        context={
            'blog_data':blog_data
        }
        return render(request,'blog/searched_objects.html',context)

 
