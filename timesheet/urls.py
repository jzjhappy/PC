'''

Created by jwang02 on 6/25/17

'''
from django.conf.urls import url
from timesheet import views as timesheet_views

urlpatterns = [
    url(r'^$', timesheet_views.Timesheet, name='timesheet'),
    url(r'^attendance/$', timesheet_views.attendance, name='attendance'),
    url(r'^grading/$', timesheet_views.grading, name='grading'),
    url(r'^advisory/$', timesheet_views.advisory, name='advisory'),
    url(r'^certificate/$', timesheet_views.certificate, name='certificate'),
    url(r'^search/$', timesheet_views.search, name='search'),
    url(r'^students_info/$', timesheet_views.students_Info, name='students_info'),
    url(r'^sum_report/$', timesheet_views.sum_Report, name='sum_report'),
]
