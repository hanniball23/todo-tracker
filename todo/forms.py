from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
            'deadline': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = ['text', 'deadline', 'progress']