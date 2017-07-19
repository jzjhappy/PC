from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from schedule.forms import ScheduleForm, ScheduleSearchForm, InstructorForm
from schedule.models import Schedules, Instructor
from schedule.tables import ScheduleTable, ScheduleListTable, InstructorTable
from django_tables2 import RequestConfig
from django.core.urlresolvers import reverse
import re
import datetime
# Create your views here.
def Schedule(request):
    return render(request, "schedule/schedule.html", {})

def schedule_List(request):
    #made search work
    context_dict = {}
    schedule_list = Schedules.objects.order_by('start_date')
    table = ScheduleListTable(schedule_list)
    context_dict['table'] = table
    return render(request, "schedule/schedule_list.html", context_dict)

def pending_Lists(request):
    return render(request, "schedule/pending_lists.html", {})

def daily_To_Do(request):
    return render(request, "schedule/daily_to_do.html", {})

def weekly_To_Do(request):
    return render(request, "schedule/weekly_to_do.html", {})

def office_Schedule(request):
    return render(request, "schedule/office_schedule.html", {})

def yearly_Schedule(request):
    return render(request, "schedule/yearly_schedule.html", {})

def start_One_Schedule(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.initiated_by = request.user.username
            obj.save()
            return render(request, 'schedule/schedule.html', {})
        else:
            print(form.errors)

    return render(request, 'schedule/start_one_schedule.html', {'form': form})

def start_Multi_Schedule(request):
    return render(request, "schedule/start_multi_schedule.html", {})

def alert_Emergency(request):
    return render(request, "schedule/alert_emergency.html", {})

def instructor_Admin(request):
    context_dict = {}
    instructor_list = Instructor.objects.order_by('first_name')
    table = InstructorTable(instructor_list)
    context_dict['table'] = table
    return render(request, "schedule/instructor_admin.html", context_dict)

def add_New_Instructor(request):
    form = InstructorForm()
    if request.method == 'POST':
        form = InstructorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'schedule/schedule.html', {})
        else:
            print(form.errors)

    return render(request, "schedule/add_new_instructor.html", {'form': form})

def delete_Schedule(request, id):
    schedule = Schedules.objects.filter(id=id).delete()
    # return HttpResponseRedirect(reverse('schedule.views.schedule_List'))
    return render(request, "schedule/schedule.html", {})

def update_Schedule(request, pk):
    schedule = get_object_or_404(Schedules, pk=pk)
    form = ScheduleForm(request.POST or None, instance=schedule)
    if form.is_valid():
        form.save()
        return redirect('schedule')
    return render(request, "schedule/update_schedule.html", {'form':form})

def search_Schedule(request):
    form = ScheduleSearchForm()
    if request.method == 'GET' and request.GET != {}:
        form = ScheduleSearchForm(request.GET)

        if form.is_valid():
            # print(form.cleaned_data)
            cleaned_form = form.cleaned_data
            schedule = Schedules.objects.none()
            for key in cleaned_form:
                value = cleaned_form[key]
                if value == '' or value == None:
                    continue
                else:
                    # print('key:'+key)
                    if schedule:
                        schedule = schedule.filter(**{key: value})
                    else:
                        schedule = Schedules.objects.filter(**{key: value})

            table = ScheduleTable(schedule)
            RequestConfig(request, paginate={'per_page': 2}).configure(table)
            return render(request, 'schedule/search_schedule.html', {'form': form, 'table': table})
        else:
            print(form.errors)
    return render(request, 'schedule/search_schedule.html', {'form': form})
    # context_dict = {}
    # if request.method == 'POST':
    #     query1 = request.POST['course_name_search']
    #     query2 = request.POST['start_date_search']
    #     query3 = request.POST['instructor_search']
    #     if query1:
    #         results = Schedules.objects.filter(course_name__icontains=query1)
    #         if query2:
    #             results = results.filter(start_date=query2)
    #             if query3:
    #                 results = results.filter(instructor__icontains=query3)
    #                 table = ScheduleTable(results)
    #                 if results.count():
    #                     context_dict['table'] = table
    #                 else:
    #                     context_dict['no_results'] = query1 + ", " + query2 + ", and " + query3
    #             else:
    #                 table = ScheduleTable(results)
    #                 if results.count():
    #                     context_dict['table'] = table
    #                 else:
    #                     context_dict['no_results'] = query1 + " and " + query2
    #         elif query3:
    #             results = results.filter(instructor__icontains=query3)
    #             table = ScheduleTable(results)
    #             if results.count():
    #                 context_dict['table'] = table
    #             else:
    #                 context_dict['no_results'] = query1 + " and " + query3
    #         else:
    #             table = ScheduleTable(results)
    #             if results.count():
    #                 context_dict['table'] = table
    #             else:
    #                 context_dict['no_results'] = query1
    #     elif query2:
    #         results = Schedules.objects.filter(start_date=query2)
    #         if query3:
    #             results = results.filter(instructor__icontains=query3)
    #             table = ScheduleTable(results)
    #             if results.count():
    #                 context_dict['table'] = table
    #             else:
    #                 context_dict['no_results'] = query2 + " and " + query3
    #         else:
    #             table = ScheduleTable(results)
    #             if results.count():
    #                 context_dict['table'] = table
    #             else:
    #                 context_dict['no_results'] = query2
    #     elif query3:
    #         results = Schedules.objects.filter(instructor__icontains=query3)
    #         table = ScheduleTable(results)
    #         if results.count():
    #             context_dict['table'] = table
    #         else:
    #             context_dict['no_results'] = query3
    # return render(request, "schedule/search_schedule.html", context_dict)