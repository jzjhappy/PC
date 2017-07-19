'''

Created by jwang02 on 6/25/17

'''
from django.conf.urls import url
from wai_wdp import views as wai_wdp_views

urlpatterns = [
    url(r'^$', wai_wdp_views.Wai_Wdp, name='wai_wdp'),
    url(r'^search/$', wai_wdp_views.search, name='search'),
    url(r'^active_contracts/$', wai_wdp_views.active_Contracts, name='active_contracts'),
    url(r'^contracts_history/$', wai_wdp_views.contracts_History, name='contracts_history'),
    url(r'^edit_cip/$', wai_wdp_views.edit_Cip, name='edit_cip'),
    url(r'^view_report/$', wai_wdp_views.view_Report, name='view_report'),
]
