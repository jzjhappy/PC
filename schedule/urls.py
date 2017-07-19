'''

Created by jwang02 on 6/25/17

'''
from django.conf.urls import url
from schedule import views as schedule_views

urlpatterns = [
    url(r'^$', schedule_views.Schedule, name='schedule'),
    url(r'^schedule_list/$', schedule_views.schedule_List, name='schedule_list'),
    url(r'^pending_lists/$', schedule_views.pending_Lists, name='pending_lists'),
    url(r'^daily_to_do/$', schedule_views.daily_To_Do, name='daily_to_do'),
    url(r'^weekly_to_do/$', schedule_views.weekly_To_Do, name='weekly_to_do'),
    url(r'^office_schedule/$', schedule_views.office_Schedule, name='office_schedule'),
    url(r'^yearly_schedule/$', schedule_views.yearly_Schedule, name='yearly_schedule'),
    url(r'^start_one_schedule/$', schedule_views.start_One_Schedule, name='start_one_schedule'),
    url(r'^start_multi_schedule/$', schedule_views.start_Multi_Schedule, name='start_multi_schedule'),
    url(r'^alert_emergency/$', schedule_views.alert_Emergency, name='alert_emergency'),
    url(r'^instructor_admin/$', schedule_views.instructor_Admin, name='instructor_admin'),
    url(r'^update_schedule/(?P<pk>\d+)$', schedule_views.update_Schedule, name='update_schedule'),
    url(r'^delete_schedule/(?P<id>\d+)/$', schedule_views.delete_Schedule, name='delete_schedule'),
    url(r'^search_schedule/$', schedule_views.search_Schedule, name='search_schedule'),
    url(r'^add_new_instructor/$', schedule_views.add_New_Instructor, name='add_new_instructor'),
]