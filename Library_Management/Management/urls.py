from os import name
from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('',views.home, name='home'), 
    path('accounts/login/',views.login_view, name='login'),
    path('accounts/signup/',views.signup, name='signup'),


    path('accounts/stulogin/',views.stu_login, name='stu_login'),

    path('accounts/stu_signup/',views.stu_signup, name='stu_signup'),

    path('homepage',views.homepg, name='homepg'),
    path('contact',views.contact, name='contact'),
    
    path('addbook',views.addbooks,name='addbooks'),
    path('viewbook',views.viewbooks,name='viewbooks'),
    path('delete/<int:id>/',views.delete_data,name="deletedata"), 
    path('updatedata/<str:pk>/',views.update_data,name="updatedata"),

    path('issuebook',views.issuebooks,name='issuebooks'),
    path('viewissuebook',views.viewissuebooks,name='viewissuebooks'),
    path('delete/<int:id>/',views.deleteissue_data,name="deletedata"), 
    path('updateissuedata/<str:pk>/',views.updateissue_data,name="updateissuedata"),

    path('addstudent',views.addstudents,name='addstudents'),
    path('viewstudent',views.viewstudents,name='viewstudents'),
    #path('editbook',views.editbooks,name='editbooks'),

    path('stuhomepage',views.stuhomepg,name='stuhomepg'),
    path('stuviewissuebook',views.stuviewissuebooks,name='stuviewissuebooks'),
    path('fan1learnmore',views.fan1learnmores,name='fan1learnmores'),
    path('fantwolearnmore',views.fantwolearnmores,name='fantwolearnmores'),
    path('fanthreelearn',views.fanthreelearns,name='fanthreelearns'),
    path('fanfoure',views.fanfoures,name='fanfoures'),
    path('eduone',views.eduones,name='eduones'),
    path('edutwo',views.edutwos,name='edutwos'),
    path('eduthree',views.eduthrees,name='eduthrees'),
    path('edufour',views.edufours,name='edufours'),
    path('bioone',views.bioones,name='bioones'),
    path('biotwo',views.biotwos,name='biotwos'),
    path('biothree',views.biothrees,name='biothrees'),
    path('biofour',views.biofours,name='biofours'),
    path('details',views.details,name='details'),

    path('edu&ref',views.edu_ref,name='edu_ref'),
    
    
    
   
      
]
