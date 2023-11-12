from django.db import models
from blog.models import User


class Creating_blog(models.Model):
    id = models.AutoField(primary_key=True)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogger',blank=True,null=True)
    blog_title = models.CharField(max_length=300,verbose_name='Blog Title')
    blog_content = models.TextField(verbose_name = 'Write Your Blog ')
    blog_image = models.ImageField(upload_to='image_blog')
    slug = models.SlugField(max_length = 400, unique=True)
    published_data = models.DateField(auto_now_add= True)
    update_date = models.DateField(auto_now=True)
