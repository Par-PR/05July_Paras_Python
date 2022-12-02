from django import forms
from .models import Signup,mynotes


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'
        
class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'
    
class updateForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields=['firstname','lastname','username','password','city','state','mobile']