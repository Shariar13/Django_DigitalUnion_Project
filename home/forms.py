from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import ListView, TemplateView, UpdateView
from django.contrib.auth.models import User
from .models import post




class edit_post(forms.ModelForm):
    status=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    

    class Meta:
        model = post
        fields = ('status',)


