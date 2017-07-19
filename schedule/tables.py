import django_tables2 as tables
from schedule.models import Schedules, Instructor

class ScheduleTable(tables.Table):
    class Meta:
        model = Schedules
        exclude = ('id',)
        attrs = {'class': 'table table-striped', 'id': 'schedule'}

class ScheduleListTable(tables.Table):
    change = tables.TemplateColumn('''<a href="/schedule/update_schedule/{{ record.id }}">Update</a> / Event /
                                   <a href="/schedule/delete_schedule/{{ record.id }}" onclick="return confirm('Are you sure you want to delete this?')">Delete</a>''',
                                   verbose_name=u'Change', )
    class Meta:
        model = Schedules
        fields = ('schedule_id', 'course_name', 'start_date', 'start_time', 'hours_per_class', 'instructor', 'change',)
        attrs = {'class': 'table table-striped', 'id': 'schedule_list'}

class InstructorTable(tables.Table):
    name = tables.TemplateColumn('''{{ record.first_name }} {{ record.last_name }}''', verbose_name=u'Name', )
    home_phone = tables.TemplateColumn(
        '''{{ record.home_phone_area }}-{{ record.home_phone_prefix }}-{{ record.home_phone_line }}''',
        verbose_name=u'Home Phone', )
    work_phone = tables.TemplateColumn(
        '''{{ record.work_phone_area }}-{{ record.work_phone_prefix }}-{{ record.work_phone_line }} Ext:{{ record.work_phone_ext }}''',
        verbose_name=u'Work Phone', )
    cell_phone = tables.TemplateColumn(
        '''{{ record.cell_phone_area }}-{{ record.cell_phone_prefix }}-{{ record.cell_phone_line }}''',
        verbose_name=u'Cell Phone', )
    manage = tables.TemplateColumn('''Update / Delete''',
        verbose_name=u'Manage', )
    class Meta:
        model = Instructor
        fields = ('name', 'email', 'home_phone', 'work_phone', 'cell_phone', 'type', 'status', 'manage',)
        attrs = {'class': 'table table-striped', 'id': 'instructor'}