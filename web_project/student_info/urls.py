from django.urls import path
from . import views

app_name = 'student_info'

urlpatterns = [
    path('',views.index, name='index'),
    path('send/',views.sending, name = 'sending'),

]