from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home.as_view(),name="home"),
    path('comments/<int:pk>',views.comments.as_view(),name="comments"),
    path('comment_form',views.comment_form,name="comment_form"),
    path('comment/<int:pk>/delete',views.delete_comment.as_view(),name='delete_comment'),
    path('profile',views.profile.as_view(),name='profile'),
    path('status_form',views.status_form,name='status_form'),
    path('edit/<int:pk>',views.edit.as_view(),name='edit'),
    path('post/<int:pk>/delete',views.delete.as_view(),name='delete'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('gallary/',views.gallary,name='gallary'),
    path('complain_box/',views.complain_box.as_view(),name="complain_box"),
    path('complain_form/',views.complain_form,name='complain_form'),
    path('project/',views.project.as_view(),name='project'),
    path('project_form/',views.project_form,name='project_form'),
    

    
    
]