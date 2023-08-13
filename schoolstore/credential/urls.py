from . import views
from django.urls import path

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('button', views.button, name='button'),
    path('left', views.left, name='left'),
    path('frm', views.frm, name='frm'),
    path('msg', views.msg, name='msg'),

]
