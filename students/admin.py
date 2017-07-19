from django.contrib import admin
from students.models import Student, StudentCourse, StudentEmployment, CourseCategory, Course


class StudentAdmin(admin.ModelAdmin):
	list_display = ('student_id', 'first_name', 'last_name', 'zipcode', 'city', 'state')

class StudentCourseAdmin(admin.ModelAdmin):
	list_display = ('student', 'course')

class StudentEmploymentAdmin(admin.ModelAdmin):
	list_display = ('student', 'company', 'title')

class CourseCategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)

class CourseAdmin(admin.ModelAdmin):
	list_display = ('course_id', 'name', 'category')


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)
admin.site.register(StudentEmployment, StudentEmploymentAdmin)
admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(Course, CourseAdmin)
