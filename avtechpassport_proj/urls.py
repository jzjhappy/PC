"""avtechpassport_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from avtechpassport import views as  avtechpassport_views
# from students import views as  students_views
from material.frontend import urls as frontend_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.login, name='login'),
    url(r'', include(frontend_urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^avtechpassport/', include('avtechpassport.urls')),
    # url(r'^students/', students_views.students, name='student'), # I replaced with include
    url(r'^administration/', include('administration.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^billing/', include('billing.urls')),
    url(r'^timesheet/', include('timesheet.urls')),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^wai_wdp/', include('wai_wdp.urls')),
    url(r'^schedule/', include('schedule.urls')),
]

