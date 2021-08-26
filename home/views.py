from urllib.parse import quote
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from .models import post
from .models import comment
from django.views import generic
from django.urls import reverse_lazy
from .forms import edit_post
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from .models import complain






class home(ListView):
    template_name = "index.html"
    model = post
    ordering = ['-id']

class profile(ListView):
    template_name = "adminpanel.html"
    model = post
    ordering = ['-id']

class edit(UpdateView):
    model=post
    form_class=edit_post
    template_name = 'edit.html'

class complain_box(ListView):
    template_name = "complain_box.html"
    model = complain
    ordering = ['-id']

class delete(DeleteView):
    model = post
    template_name = 'delete.html'
    fields = ['status']
    success_url = reverse_lazy('profile')

def status_form(request):
        if request.method=="POST":
                username=request.POST['username']
                statuss=request.POST['status_name']
                name=request.POST['name']
                email=request.POST['email']
                if statuss=='':
                        return HttpResponse('404 not found.You must be write something!')
                else:
                        status_database=post(post_author=username,status=statuss,author_name=name,author_email=email)
                        status_database.save()
                        return redirect('profile')
    
    
class comments(generic.DetailView):
    model = post
    template_name = 'comment.html'
    ordering = ['-id']
    

  

    def get_context_data(self, *args, **kwargs):
        context = super(comments, self).get_context_data(*args, **kwargs)
        context['comment_list'] = comment.objects.all()
        return context



def comment_form(request):
    if request.method=="POST":
        commentss=request.POST['comment_name']
        commenter=request.POST['commenter_name']
        commenter_username=request.POST['commenter_username']
        comment_id=request.POST['id']
        post_author_name=request.POST['post_author_name']
        comment_database=comment(comment=commentss,commenter_name=commenter,comment_id=comment_id,post_author_name=post_author_name,commenter_username=commenter_username)
        comment_database.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def complain_form(request):
    if request.method=="POST":
        name=request.POST['name']
        if name == "":
            messages.error(request,"Name field can not be empty")
            return redirect('complain_box')
        phone=request.POST['phone']
        if phone == "":
            messages.error(request,"Phone Number field can not be empty")
            return redirect('complain_box')
        village=request.POST['village']
        if village == "":
            messages.error(request,"Village field can not be empty")
            return redirect('complain_box')
        word=request.POST['word']
        if word == "":
            messages.error(request,"Word field can not be empty")
            return redirect('complain_box')
        complains=request.POST['complains']
        if complains == "":
            messages.error(request,"Complain field can not be empty")
            return redirect('complain_box')
        complain_database=complain(name=name,phone=phone,village=village,word=word,complain=complains)
        complain_database.save()
        messages.success(request,"We have received your complain & we will contact soon.")
        return redirect('complain_box')
        

class delete_comment(DeleteView):
    model = comment
    template_name = 'delete_comment.html'
    fields = ['comment']
    # success_url=reverse_lazy("comments/53")
    def get_context_data(self, *args, **kwargs):
        context = super(delete_comment, self).get_context_data(*args, **kwargs)
        context['post'] = post.objects.all()
        return context
    success_url=("http://127.0.0.1:8000/comments/{comment_id}")

def about (request):
    return render (request, "about.html")

def contact (request):
    return render (request, "contact.html")

def gallary (request):
    return render (request, "gallary.html")


