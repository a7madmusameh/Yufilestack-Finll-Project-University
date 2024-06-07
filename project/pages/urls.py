from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admins',views.admins,name='admins'),
    path('signup',views.signup,name='signup'),
    path('cis',views.cis,name='cis'),
    path('cs',views.cs,name='cs'),
    path('bit',views.bit,name='bit'),
    path('search',views.search,name='search'),
    path('subject',views.subject,name='subject'),
    path('subject1',views.subject1,name='subject1'),
    path('subject2',views.subject2,name='subject2'),
    path('login',views.login,name='login'),
]