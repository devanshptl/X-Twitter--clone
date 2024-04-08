from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Talkform(forms.ModelForm):
    body = forms.CharField(required=True,
    widget=forms.widgets.Textarea(
        attrs={
            "placeholder": "Write talks here..",
            "class":"form-control"
        }
    ),
    label="",
    )

    class Meta:
        model = Talks
        exclude = ('user','likes','dislikes', )



class createprofileform(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Pic',required=False)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email',"class":"form-control"}))
    mobile_no = forms.CharField(label='Mobile Number', max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Enter your mobile number',"class":"form-control"}))
    about = forms.CharField(label='About',max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter description',"class":"form-control"}))
    class Meta:
        model = Profile
        exclude = ('user',)

    

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)

	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['username'].widget.attrs['placeholder'] = 'Enter user Name'
	    self.fields['username'].label = 'User Name:'
	    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

	    self.fields['password1'].widget.attrs['class'] = 'form-control'
	    self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
	    self.fields['password1'].label = 'Paaword:'
	    self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

	    self.fields['password2'].widget.attrs['class'] = 'form-control'
	    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
	    self.fields['password2'].label = 'Password confirmation:'
	    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'