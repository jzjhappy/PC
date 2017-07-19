'''
Created on May 29, 2017

@author: jwang02
'''
# django import
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.forms.models import model_to_dict

# third party import
from django_tables2 import RequestConfig

# custom import
from students.models import Student, StudentCourse, Course, StudentEmployment
from students.forms import StudentForm, StudentCourseForm, StudentEmploymentForm, StudentSearchForm
from students.tables import StudentTable


@login_required
def Students(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.

    # Render the response and send it back!
	student = Student.objects.all()[:5]
	table = StudentTable(student)
	RequestConfig(request).configure(table)
	return render(request, 'students/students.html', {'table': table})


def add_Student(request):
	form = StudentForm()
	if request.method == 'POST':
		form = StudentForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			# Step 1 complete. Return student id, etc. Move to success page.
			context_dict = {'student_id': form['student_id'].value, 'first_name': form['first_name'].value, 'last_name': form['last_name'].value}
			return render(request, 'students/add_student_success.html', context_dict )
		else:
			print(form.errors)

	return render(request, 'students/add_student.html', {'form': form})


def add_StudentCourse(request, identify):
	try:
		student = Student.objects.get(student_id=identify)
	except Student.DoesNotExist:
		student = None

	if student:
		form = StudentCourseForm()
		if request.method == 'POST':
			form = StudentCourseForm(request.POST)
			if form.is_valid():
				# print('form is valid!')
				# print(form.cleaned_data)
				for key in form.cleaned_data:
					cat = key
					courses = form.cleaned_data[cat]
					# print(cat, courses)
					if courses != []:
						for each in courses:
							print("now creating course: "+each)
							each_slug = slugify(each)
							studentcourse = StudentCourse()
							studentcourse.student = student
							studentcourse.course = Course.objects.get(slug=each_slug)
							studentcourse.save()

				context_dict = {'student_id': student.student_id, 'first_name': student.first_name, 'last_name': student.last_name}
				return render(request, 'students/add_studentcourse_success.html', context_dict)		

			else:
				print(form.errors)
		print(form)
		return render(request, 'students/add_studentcourse.html', {'form': form, 'student_id': identify})

	else:
		print("We can't find the student. Please add a student.")
		return render(request, 'students/add_student.html')


def add_StudentEmployment(request, identify):
	try:
		student = Student.objects.get(student_id=identify)
	except Student.DoesNotExist:
		student = None

	if student:
		form = StudentEmploymentForm()
		if request.method == 'POST':
			form = StudentEmploymentForm(request.POST)
			if form.is_valid():
				employment = form.save(commit=False)
				employment.student = student
				employment.save()

				context_dict = {'student_id': student.student_id, 'first_name': student.first_name, 'last_name': student.last_name}
				return render(request, 'students/add_studentemployment_success.html', context_dict)
			else:
				print(form.errors)

		return render(request, 'students/add_studentemployment.html', {'form': form, 'student_id': identify})
		
	else:
		print("Can't find this student. Please create student info.")
		return render(request, "students/add_student.html")


def search_student(request):
	form = StudentSearchForm()
	if request.method == 'GET' and request.GET != {}:
		form = StudentSearchForm(request.GET)

		if form.is_valid():
			# print(form.cleaned_data)
			cleaned_form = form.cleaned_data
			student = Student.objects.none()
			for key in cleaned_form:
				value = cleaned_form[key]
				if value == '' or value == None:
					continue
				else:
					# print('key:'+key)
					if student:
						student = student.filter(**{key: value})
					else:
						student = Student.objects.filter(**{key: value})

			table = StudentTable(student)
			RequestConfig(request, paginate={'per_page': 2}).configure(table)
			return render(request, 'students/search_student.html', {'form': form, 'table': table})
		else:
			print(form.errors)

	return render(request, 'students/search_student.html', {'form': form})


def view_student(request, identify):
	print('student_id: '+identify)
	try:
		student = Student.objects.get(student_id=identify)
	except Student.DoesNotExist:
		student = None

	if student:
		student = model_to_dict(student)
		print(student)
		courses = StudentCourse.objects.filter(student__student_id=identify)
		employments = StudentEmployment.objects.filter(student__student_id=identify)
		context_dic = {'student': student, 'courses': courses, 'employments': employments}
		return render(request, 'students/view_student.html', context_dic)
	else:
		return HttpResponse('Can not find this student. Please provide valid student id.')


def test(request):
	if request.GET:
		print(request.GET['sort'])
	student = Student.objects.all()
	table = StudentTable(student)
	print(', '.join(map(str, table.rows[0])))
	RequestConfig(request).configure(table)
	return render(request, 'students/test.html', {'table': table})