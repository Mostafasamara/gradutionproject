from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True,blank=False)
    title = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)


    class Meta:
        ordering = ('created', )



class Task(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    project = models.ForeignKey('Project',related_name='tasks',on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User',related_name='tasks',on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=False,null=True)
    end = models.DateTimeField(auto_now_add=False,null=True)
    desc = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

class Group(models.Model):
    title = models.CharField(max_length=100,blank=False,default='')
    project = models.ForeignKey('Project',related_name='groups',on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User',related_name='group',on_delete=models.CASCADE)
    member = models.ManyToManyField('auth.User',related_name='group_members')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
