'''
Created on May 29, 2017

@author: jwang02
'''
from django.conf.urls import url
from students import views as students_views

urlpatterns = [
    url(r'^$', students_views.Students, name='students'),
    url(r'^add_student/$', students_views.add_Student, name='add_student'),
    url(r'^id=(?P<identify>[\w]+)/add_studentcourse/$', students_views.add_StudentCourse, name='add_studentcourse'),
    url(r'^id=(?P<identify>[\w]+)/add_studentemployment/$', students_views.add_StudentEmployment, name='add_studentemployment'),
    url(r'test/$', students_views.test, name='test'),
    url(r'search_student/$', students_views.search_student, name='search_student'),
    # url(r'^/edit/', students_views.edit_student, name='edit_student'),
    # url(r'', students_views.delete_student, name='delete_student'),
    url(r'^view/student_id=(?P<identify>[\w]+)', students_views.view_student, name='view_student'),
]

