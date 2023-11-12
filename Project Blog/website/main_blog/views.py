from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import CreateView,UpdateView
from main_blog.models import Creating_blog
from blog.models import User
from django.urls import reverse
import uuid
from django.db.models.functions import Replace
from django.db.models import Value
# Create your views here.
def blog_list(request):
    blog_items = Creating_blog.objects.filter( blogger=request.user)

    context = {
        'blog_items':blog_items
    }
    return render(request,'create_blog/display_blogs.html',context)
    
class CreateBlog (CreateView):
    model = Creating_blog
    template_name = 'create_blog/create_blog.html'
    fields = ('blog_title','blog_content','blog_image',)

    def form_valid(self,form):
        form_obj = form.save(commit = False)
        form_obj.blogger = self.request.user
        title = form_obj.blog_title
        form_obj.slug = title.replace(' ', '-') + '/' + str(uuid.uuid4())
        form_obj.save()
        return redirect('blog_list')


def read_blog(request,id):
    try:
        data = Creating_blog.objects.get(id=id)
        context = {
        'data':data
        }
        print(data.slug)
        print(type(data.slug))

        return render(request,'create_blog/read_blog.html',context)
    except:
        return HttpResponse("No data avaulable")

def view_blog_profile(request,id):
    user = User.objects.get(id = id)
    data = Creating_blog.objects.filter(blogger = user)
    print(data)
    print("Checked successfully ")

    context = {
        'data':data,
        'user':user
    }
    return render(request,'create_blog/blog_profile.html',context)


def read_blog_slug(request,slug):
    try:
        data = Creating_blog.objects.get(slug=slug)
        context = {
        'data':data
        }

        return render(request,'create_blog/read_blog.html',context)
    except:
        return HttpResponse("No data avaulable")
