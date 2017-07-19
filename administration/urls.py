'''

Created by jwang02 on 7/16/17

'''

from django.conf.urls import url
from administration import views as administration_views

urlpatterns = [
    url(r'^$', administration_views.administration, name='administration'),
]

