
from blog.models import profile
from django import forms


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = profile
        fields = ['first_name','last_name','profile_pic']
        labels = {
        "first_name":  "First Name",
        "last_name": "Last Name",
        
    }
