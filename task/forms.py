from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'task_description',
            'due_date',

        ]
        labels = {
            'title': 'Task Title',
            'task Description': 'Add description here',
            'due_date': 'Due Date (optional)',
        }
        widgets = {
            'task_description': forms.Textarea(attrs={'cols': 80}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CustomUserProfile(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Enter valid email address.')
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]