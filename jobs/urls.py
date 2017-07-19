'''

Created by jwang02 on 6/25/17

'''
from django.conf.urls import url
from jobs import views as  jobs_views

urlpatterns = [
    url(r'^$', jobs_views.Jobs, name='jobs'),
    url(r'^student_resume/$', jobs_views.student_Resume, name='student_resume'),
    url(r'^skills_list/$', jobs_views.skills_List, name='skills_list'),
    url(r'^clients/$', jobs_views.clients, name='clients'),
    url(r'^positions/$', jobs_views.positions, name='positions'),
    url(r'^group_email/$', jobs_views.group_Email, name='group_email'),
]