from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Project,Task,Group

@admin.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','created','owner']


@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','project','owner','start','end','desc']

@admin.register(Group)

class GroupAdmin(admin.ModelAdmin):
    fields = ['members']
    list_display = ['title' ,'owner' ,'created' ,'active', 'project']

    def get_members(self, obj):
        return "\n".join([m.members for m in obj.members.all()])
