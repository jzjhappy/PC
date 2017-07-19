'''

Created by jwang02 on 6/25/17

'''
from django.conf.urls import url
from billing import views as  billing_views

urlpatterns = [
    url(r'^$', billing_views.Billing, name='index'),
    url(r'^pay_tuition', billing_views.pay_Tuition, name='pay_tuition'),
    url(r'^payment_notice', billing_views.payment_Notice, name='payment_notice'),
    url(r'^sales_log', billing_views.sales_Log, name='sales_log'),
]