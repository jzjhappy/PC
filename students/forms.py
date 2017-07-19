# django import
from django import forms
from django.core.validators import validate_email, MinValueValidator
# third party import
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import USStateField, USSocialSecurityNumberField, USZipCodeField
from django_countries import countries
# custom import
from students.models import Student, StudentEmployment
from students.choices import *


class StudentForm(forms.ModelForm):
	# STEP 1 FORM
	# student_id = forms.CharField(max_length=128, label="Student ID")
	first_name = forms.CharField(max_length=128, label="First Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=128, label="Last Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
	ssn = USSocialSecurityNumberField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="SSN", help_text="Format: xxx-xx-xxxx")
	gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
	dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label="Date of birth", help_text="Format: yyyy-mm-dd")
	address = forms.CharField(max_length=128, label="Address")
	city = forms.CharField(max_length=128, label="City")
	state = forms.ChoiceField(choices=STATE_CHOICES, initial="NJ", label="State")
	zipcode = USZipCodeField(label="Zipcode")
	country = forms.ChoiceField(choices=countries, label="Country", initial="US")
	primary_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bfh-phone', 'data-format': '+1 (ddd) ddd-dddd'}), max_length=128, label="Primary phone")
	secondary_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bfh-phone', 'data-format': '+1 (ddd) ddd-dddd'}), max_length=128, label="Secondary phone")
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'name':"email", 'id':"email"}), max_length=254, validators=[validate_email], label="Email")
	background = forms.ChoiceField(choices=BACKGROUND_CHOICES, label="Background")
	location = forms.ChoiceField(choices=LOCATION_CHOICES, initial="south_plainfield", label="Location")
	workforce = forms.ChoiceField(choices=WORKFORCE_CHOICES, initial="--", label="Workforce")
	source = forms.ChoiceField(choices=SOURCE_CHOICES, initial="individual", label="Source")
	refer_by = forms.ChoiceField(choices=REFER_BY_CHOICES, initial="no refer", label="Refer by")
	last_status = forms.ChoiceField(choices=LAST_STATUS_CHOICES, initial="followup", label="Last status")
	newsletter = forms.BooleanField(widget=forms.CheckboxInput(), label="Newsletter", required=False)
	created_by = forms.CharField(widget=forms.HiddenInput(), label="", max_length=32)
	date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label="Date", help_text="Format: yyyy-mm-dd")
	notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False, label="Notes", help_text="less than 1000 characters")

	class Meta:
		model = Student
		fields = ('student_id', 'first_name', 'last_name', 'ssn', 'gender', 'dob', 'address', 'city', 'state', 'zipcode', 'country', 'primary_phone', 'secondary_phone', 'email', 'background', 'location', 'workforce', 'source', 'refer_by', 'last_status', 'newsletter', 'date', 'notes')


class StudentCourseForm(forms.Form):
	# STEP 2 COURSE INFO
	# student = models.ForeignKey(Student)
	networking = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=NETWORKING_CHOICES, required=False)
	system_admin = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=SYSTEM_ADMIN_CHOICES, required=False)
	database = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=DATABASE_CHOICES, required=False)
	programming = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=PROGRAMMING_CHOICES, required=False)
	accounting = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=ACCOUNTING_CHOICES, required=False)
	office_skill = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=OFFICE_SKILL_CHOICES, required=False)
	graphic = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=GRAPHIC_CHOICES, required=False)
	management = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=MANAGEMENT_CHOICES, required=False)
	miscellaneous = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=MISCELLANEOUS_CHOICES, required=False)
	notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=1024, required=False, help_text="less than 1024 characters")


class StudentEmploymentForm(forms.ModelForm):
	# STEP 3 EMPLOYMENT INFO

	# company = forms.CharField(max_length=128, required=False)
	# title = forms.CharField(max_length=128, required=False)
	# supervisor = forms.CharField(max_length=128, required=False)
	doh = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), label="Date of hire", help_text='yyyy-mm-dd', required=False)
	# hourly_salary = models.FloatField(required=False)
	hpw = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), validators=[MinValueValidator(1)], label="hours per week", required=False)
	# address = forms.CharField(max_length=128, required=False)
	# city = forms.CharField(max_length=128, required=False)
	# state = forms.ChoiceField(choices=STATE_CHOICES, initial='NJ', required=False)
	# zipcode = USZipCodeField(required=False)
	# country = forms.ChoiceField(choices=countries, initial='US', required=False)
	# work_phone = forms.CharField(max_length=128, required=False)
	# work_phone_ext = forms.CharField(max_length=128, required=False)
	# fax = forms.CharField(max_length=128, required=False)
	fbr = forms.NullBooleanField(widget=forms.NullBooleanSelect(attrs={'class': 'form-control'}), label="fringe benefits received", required=False)
	cbub = forms.NullBooleanField(widget=forms.NullBooleanSelect(attrs={'class': 'form-control'}), label="covered by unemployment benefits", required=False)
	# placed_by = forms.ChoiceField(choices=PLACED_BY_CHOICES, required=False)
	training_related = forms.NullBooleanField(widget=forms.NullBooleanSelect(attrs={'class': 'form-control'}), required=False)
	notes = forms.CharField(max_length=1024, widget=forms.Textarea(attrs={'class': 'form-control'}), required=False, help_text="less than 1024 characters")

	class Meta:
		model = StudentEmployment
		fields = ('company', 'title', 'supervisor', 'doh', 'hourly_salary', 'hpw', 'address', 'city', 'state', 'zipcode', 'country', 'work_phone', 'work_phone_ext', 'fax', 'fbr', 'cbub', 'placed_by', 'training_related', 'notes')
		exclude = ('student',)

		# widges and bootstrap .class
		textinput_widget = ['company', 'title', 'supervisor', 'hourly_salary', 'address', 'city', 'state', 'zipcode', 'work_phone', 'work_phone_ext', 'fax']
		widgets = {}
		for count in range(len(textinput_widget)):
			widgets[textinput_widget[count]] = forms.TextInput(attrs={'class': 'form-control'})

		select_widget = ['state', 'country', 'placed_by']
		for count in range(len(select_widget)):
			widgets[select_widget[count]] = forms.Select(attrs={'class': 'form-control'})


class StudentSearchForm(forms.Form):
	student_id = forms.CharField(max_length=64, required=False)
	ssn = USSocialSecurityNumberField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="SSN", help_text="Format: xxx-xx-xxxx", required=False)
	first_name = forms.CharField(max_length=128, required=False)
	last_name = forms.CharField(max_length=128, required=False)
	course = forms.ChoiceField(choices=STUDENT_SEARCH_COURSES, required=False)
	location = forms.ChoiceField(choices=STUDENT_SEARCH_LOCATION_CHOICES, required=False)
	date_of_birth = forms.DateField(help_text='yyyy-mm-dd', required=False)
	gender = forms.ChoiceField(choices=STUDENT_SEARCH_GENDER_CHOICES, required=False)