from django.contrib import admin
from task.models import Task

# Register your models here.
admin.site.site_header = "Task Management Admin"

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'created_at', 'due_date', 'completed'
    )
    list_filter = ('completed', 'due_date')
    search_fields = ('title', 'task_description')
