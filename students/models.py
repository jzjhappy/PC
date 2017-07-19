# python import
import random
import string

# django import
from django.db import models
from django.core.validators import validate_email
from django.template.defaultfilters import slugify

# third party import
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField, USSocialSecurityNumberField, USZipCodeField
from django_countries.fields import CountryField

# customize import
from students.choices import * # instore all choices in models

# import end

class Student(models.Model):
	# STEP 1 BASIC INFO
	student_id = models.CharField(max_length=128, unique=True)
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	ssn = USSocialSecurityNumberField(null=False)
	gender = models.CharField(max_length=128, choices=GENDER_CHOICES)
	dob = models.DateField(auto_now=False, auto_now_add=False, db_column="date of birth")
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	state = USStateField(choices=STATE_CHOICES, default='NJ')
	zipcode = USZipCodeField(blank=True)
	country = CountryField(default='US', blank=True)
	primary_phone = models.CharField(max_length=16)
	secondary_phone = models.CharField(max_length=16)
	email = models.EmailField(max_length=254, validators=[validate_email])
	background = models.CharField(max_length=128, choices=BACKGROUND_CHOICES)
	location = models.CharField(max_length=128, choices=LOCATION_CHOICES, default='south_plainfield')
	workforce = models.CharField(max_length=128, choices=WORKFORCE_CHOICES, default='--')
	source = models.CharField(max_length=128, choices=SOURCE_CHOICES, default='individual')
	refer_by = models.CharField(max_length=128, choices=REFER_BY_CHOICES, default='no refer')
	last_status = models.CharField(max_length=128, choices=LAST_STATUS_CHOICES, default='followup')
	newsletter = models.BooleanField()
	created_by = models.CharField(max_length=128)
	date = models.DateField(auto_now=False, auto_now_add=False)
	notes = models.TextField()

	def __str__(self):
		return self.first_name + self.last_name

class CourseCategory(models.Model):
	name = models.CharField(max_length=128, unique=True)
	slug = models.SlugField(blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(CourseCategory, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class Course(models.Model):
	course_id = models.CharField(max_length=128, unique=True, null=True, blank=True)
	category = models.ForeignKey(CourseCategory, null=True)
	name = models.CharField(max_length=128)
	slug = models.SlugField(blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		if self.course_id == "":
			self.course_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

		super(Course, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class StudentCourse(models.Model):
	# STEP 2 STUDENT AND COURSE
	# need to redesign. Static html and studentcourse('student', 'course')
	student = models.ForeignKey(Student)
	course = models.ForeignKey(Course)
	# networking = models.CharField(max_length=128, choices=NETWORKING_CHOICES, blank=True)
	# system_admin = models.CharField(max_length=128, choices=SYSTEM_ADMIN_CHOICES, blank=True)
	# database = models.CharField(max_length=128, choices=DATABASE_CHOICES, blank=True)
	# programming = models.CharField(max_length=128, choices=PROGRAMMING_CHOICES, blank=True)
	# accounting = models.CharField(max_length=128, choices=ACCOUNTING_CHOICES, blank=True)
	# office_skill = models.CharField(max_length=128, choices=OFFICE_SKILL_CHOICES, blank=True)
	# graphic = models.CharField(max_length=128, choices=GRAPHIC_CHOICES, blank=True)
	# management = models.CharField(max_length=128, choices=MANAGEMENT_CHOICES, blank=True)
	# miscellaneous = models.CharField(max_length=128, choices=MISCELLANEOUS_CHOICES, blank=True)
	# notes = models.TextField(blank=True)

	def __str__(self):
		return self.student.student_id + self.course.name


class StudentEmployment(models.Model):
	# STEP 3 EMPLOYMENT INFO
	student = models.ForeignKey(Student)
	company = models.CharField(max_length=128, blank=True)
	title = models.CharField(max_length=128, blank=True)
	supervisor = models.CharField(max_length=128, blank=True)
	doh = models.DateField(auto_now=False, auto_now_add=False, db_column="date of hire", blank=True, null=True)
	hourly_salary = models.FloatField(blank=True, null=True)
	hpw = models.PositiveIntegerField(db_column="hours per week", blank=True, null=True)
	address = models.CharField(max_length=128, blank=True)
	city = models.CharField(max_length=128, blank=True)
	state = USStateField(choices=STATE_CHOICES, default='NJ', blank=True)
	zipcode = USZipCodeField(blank=True)
	country = CountryField(default='US', blank=True)
	work_phone = models.CharField(max_length=128, blank=True)
	work_phone_ext = models.CharField(max_length=128, blank=True)
	fax = models.CharField(max_length=128, blank=True)
	fbr = models.NullBooleanField(db_column="fringe benefits received", blank=True, null=True)
	cbub = models.NullBooleanField(db_column="covered by unemployment benefits", blank=True, null=True)
	placed_by = models.CharField(max_length=128, choices=PLACED_BY_CHOICES, blank=True)
	training_related = models.NullBooleanField(blank=True, null=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.student.student_id + self.company

