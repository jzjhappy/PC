from django import forms
from django.forms import ModelChoiceField
from schedule.models import Schedules, Instructor
from schedule.choices import *
from functools import partial
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import USStateField, USZipCodeField
from django.core.validators import validate_email
import datetime

DateInput = partial(forms.DateInput, {'class': 'datepicker form-control'})

class InstructorForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="First Name")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Last Name")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=254, validators=[validate_email], label="Email")
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Street")
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="City")
    state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=STATE_CHOICES, initial="NJ", label="State")
    zipcode = USZipCodeField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Zipcode")
    home_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bfh-phone', 'data-format': '+1 (ddd) ddd-dddd'}), label="Home Phone")
    work_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bfh-phone', 'data-format': '+1 (ddd) ddd-dddd'}), label="Work Phone")
    cell_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bfh-phone', 'data-format': '+1 (ddd) ddd-dddd'}), label="Cell Phone")
    fax = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bfh-phone', 'data-format': '+1 (ddd) ddd-dddd'}), required=False, label="Fax")
    course = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-control'}), choices=COURSE_NAME_CHOICES, label="Course")
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=TYPE_CHOICES, label="Type")
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=INSTRUCTOR_STATUS_CHOICES, label="Status")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False, label="Description")

    class Meta:
        model = Instructor
        fields = ('first_name', 'last_name', 'email', 'street', 'city', 'state', 'zipcode', 'home_phone', 'work_phone', 'cell_phone', 'fax', 'course', 'type', 'status', 'description',)

        # textinput_widget = ['first_name', 'last_name', 'street', 'city', 'zipcode', 'home_phone_area', 'home_phone_prefix', 'home_phone_line', 'work_phone_area', 'work_phone_prefix', 'work_phone_line', 'work_phone_ext',
        #                     'cell_phone_area', 'cell_phone_prefix', 'cell_phone_line', 'fax_area', 'fax_prefix', 'fax_line']
        # widgets = {}
        # for count in range(len(textinput_widget)):
        #     widgets[textinput_widget[count]] = forms.TextInput(attrs={'class': 'form-control'})

class InstructorChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "{0} {1}".format(obj.first_name, obj.last_name)

class ScheduleForm(forms.ModelForm):
    course_name = forms.ChoiceField(choices=COURSE_NAME_CHOICES, initial='a-plus', label="Course Name", widget=forms.Select(attrs={'class': 'form-control'}))
    location = forms.ChoiceField(choices=LOCATION_CHOICES, initial='south_plainfield', label="Location", widget=forms.Select(attrs={'class': 'form-control'}))
    room = forms.ChoiceField(choices=ROOM_CHOICES, initial='A', label="Room", widget=forms.Select(attrs={'class': 'form-control'}))
    start_date = forms.DateField(input_formats=['%m/%d/%Y'], label="Start Date", widget=DateInput(format='%m/%d/%Y'), help_text="MM/DD/YYYY")
    start_time = forms.ChoiceField(choices=START_TIME_CHOICES, initial='eight-thirty am', label="Start Time", widget=forms.Select(attrs={'class': 'form-control'}))
    interval = forms.ChoiceField(choices=INTERVAL_CHOICES, initial='1 day', label="Interval", widget=forms.Select(attrs={'class': 'form-control'}))
    # hours_per_class = forms.ChoiceField(choices=HOURS_PER_CLASS_CHOICES, initial='four_and_half', label="Hours Per Class", widget=forms.Select(attrs={'class': 'form-control'}))
    total_hours = forms.ChoiceField(choices=TOTAL_HOURS_CHOICES, initial='six', label="Total Hours", widget=forms.Select(attrs={'class': 'form-control'}))
    instructor = InstructorChoiceField(queryset=Instructor.objects.all(), label="Instructor", widget=forms.Select(attrs={'class': 'form-control'}))
    end_time = forms.ChoiceField(choices=END_TIME_CHOICES, initial='eight-thirty am', label="End Time", widget=forms.Select(attrs={'class': 'form-control'}))
    frequency = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FREQUENCY_CHOICES, label="Frequency", help_text="Please select at least one")
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS_CHOICES, label="Status")

    class Meta:
        model = Schedules
        fields = ('course_name', 'instructor', 'location', 'room', 'start_date', 'start_time', 'end_time', 'interval', 'total_hours', 'frequency', 'status',)

        widgets = {}

class ScheduleSearchForm(forms.Form):
    course_name = forms.ChoiceField(choices=COURSE_NAME_CHOICES, required=False)
    start_date = forms.DateField(widget=DateInput(format='%m/%d/%Y'), required=False)
    instructor = forms.ChoiceField(choices=INSTRUCTOR_CHOICES, required=False)