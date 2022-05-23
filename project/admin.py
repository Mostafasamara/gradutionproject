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

    list_display = ['title' ,'owner' ,'created' ,'active','active']

    def get_member(self, obj):
        return "\n".join([m.member for m in obj.member.all()])


# @admin.register(Image)
# class Image(admin.ModelAdmin):
#     list_display = ['owner','file']
