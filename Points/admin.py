from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .forms import StudentCreationForm, StudentChangeForm
from .models import Student, StudentDetailPoints


class StudentAdmin(UserAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm
    model = Student
    list_display = (
        'email',
        'username',
        'second_name',
        'first_name',
        'third_name',
        'group',
        'hostel',
        'points',
        'get_html_photo'
    )

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=75>")

    get_html_photo.short_description = 'Фото пользователя'

    list_filter = (
        'email',
        'username',
        'second_name',
        'first_name',
        'third_name',
        'group',
        'hostel',
        'points',
    )
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Данные студента', {'fields': ('photo', 'first_name', 'second_name', 'third_name', 'institute', 'group', 'hostel', 'points')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'photo', 'first_name', 'second_name', 'third_name', 'institute', 'group', 'hostel', 'password1', 'password2')}
         ),
    )
    search_fields = ('first_name', 'second_name', 'points', 'group')
    ordering = ('first_name', 'second_name', 'third_name', 'points', 'hostel')


class StudentDetailPointsAdmin(admin.ModelAdmin):
    model = StudentDetailPoints
    list_display = (
        'student',
        'received_points',
        'points_activity',
        'date'
    )
    list_filter = (
        'date', 'student',
    )
    ordering = ('student', 'date')


admin.site.register(StudentDetailPoints, StudentDetailPointsAdmin)
admin.site.register(Student, StudentAdmin)

