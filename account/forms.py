from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import photo , more_user_info, follow , comments


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())

    class Meta:
        model=User
        fields = {'first_name','last_name','email','username','password1','password2'}

    field_order = ['first_name','last_name','email','username','password1','password2']

class postt(forms.ModelForm):
    class Meta :
        model = photo
        fields = ('image','caption')
 



class edit_info(forms.ModelForm):
    class Meta:
        model =  more_user_info
        fields = ('profile_photo','phone_number','bio')

class comment_form(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('comment',)
