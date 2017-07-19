from students.models import Student
import django_tables2 as tables
from django.utils.html import format_html

class StudentTable(tables.Table):
    name = tables.Column(empty_values=(), orderable=False)
    # manage = tables.Column(empty_values=())
    selection = tables.CheckBoxColumn(empty_values=(), orderable=False)

    def render_name(self, record):
        return '{} {}'.format(record.first_name, record.last_name)

    # def render_manage(self, value):
    #     return format_html('<a><span>edit</span></a>|'
    #                        '<a><span>delete</span></a>')

    def render_selection(self, record):
        return format_html('<input type="checkbox", name="selection", class="student_check", value={} />', record.student_id)


    class Meta:
        model = Student
        fields = ('student_id', 'first_name', 'last_name', 'gender', 'ssn', 'email', 'home_phone', 'date')
        attrs = {'class': 'table table-hover', 'id': 'student'}
        sequence = ('selection', 'student_id', 'name',)

