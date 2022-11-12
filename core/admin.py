from django.contrib import admin

from reversion.admin import VersionAdmin
from mptt.admin import DraggableMPTTAdmin

from core.models import Division, Employee, Post


@admin.register(Division)
class DivisionAdmin(DraggableMPTTAdmin, VersionAdmin):
    mptt_indent_field = "name"
    save_on_top = True
    save_as = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post', 'date_of_admission', 'salary', 'division')
    list_filter = ('division', 'post')
    save_on_top = True
    save_as = True
