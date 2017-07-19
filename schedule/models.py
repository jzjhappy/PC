from django.db import models
from schedule.choices import *
from schedule.find_days import get_days
from django.contrib.auth.models import User
from django.core.validators import validate_email
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField, USZipCodeField
import datetime

# Create your models here.
class Instructor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, validators=[validate_email])
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = USStateField(choices=STATE_CHOICES, default="NJ")
    zipcode = USZipCodeField(blank=True)
    home_phone = models.CharField(max_length=128)
    work_phone = models.CharField(max_length=128)
    cell_phone = models.CharField(max_length=128)
    fax = models.CharField(max_length=128)
    course = models.CharField(max_length=128)
    type = models.CharField(max_length=128, choices=TYPE_CHOICES)
    status = models.CharField(max_length=128, choices=INSTRUCTOR_STATUS_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.first_name + self.last_name

class Schedules(models.Model):
    course_name = models.CharField(max_length=128, choices=COURSE_NAME_CHOICES, default='a-plus')
    location = models.CharField(max_length=128, choices=LOCATION_CHOICES, default='south_plainfield')
    room = models.CharField(max_length=128, choices=ROOM_CHOICES, default='A')
    start_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today)
    start_time = models.CharField(max_length=128, choices=START_TIME_CHOICES, default='eight-thirty am')
    end_time = models.CharField(max_length=128, choices=END_TIME_CHOICES, default='eight-thirty am')
    instructor = models.CharField(max_length=128)
    total_hours = models.CharField(max_length=128, choices=TOTAL_HOURS_CHOICES, default='six')
    # hours_per_class = models.CharField(max_length=128, choices=HOURS_PER_CLASS_CHOICES, default='four_and_half')
    frequency = models.CharField(max_length=128)
    status = models.CharField(max_length=128, choices=STATUS_CHOICES)
    interval = models.CharField(max_length=128, choices=INTERVAL_CHOICES, default='1 day')
    initiated_by = models.CharField(max_length=128, null=True)
    schedule_id = models.IntegerField(default=0)

    def save(self, flag=True, *args, **kwargs):
        super(Schedules, self).save()
        if flag:
            self.schedule_id = self.id + 10000
            self.save(flag=False, *args, **kwargs)

    @property
    def end_date(self):
        days = get_days(self.interval)
        return self.start_date + datetime.timedelta(days=days)

    def __str__(self):
        return self.course_name

class Event(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, validators=[validate_email])
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = USStateField(choices=STATE_CHOICES, default="NJ")
    zipcode = USZipCodeField(blank=True)
    home_phone = models.CharField(max_length=128)
    work_phone = models.CharField(max_length=128)
    cell_phone = models.CharField(max_length=128)
    fax = models.CharField(max_length=128)
    course = models.CharField(max_length=128)
    type = models.CharField(max_length=128, choices=TYPE_CHOICES)
    status = models.CharField(max_length=128, choices=INSTRUCTOR_STATUS_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.first_name + self.last_name

