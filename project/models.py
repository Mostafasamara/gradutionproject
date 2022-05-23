from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    title = models.CharField(max_length=100,blank=False,default='')
    # project = models.OneToOneField('Project',related_name='groups',on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User',related_name='groups_owner',on_delete=models.CASCADE)
    member = models.ManyToManyField('auth.User',related_name='groups_members')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    def get_member(self):
        return "\n".join([p.member for p in self.member.all()])

class Project(models.Model):
    """
    here we have all projects data and the owner of the project we can add more fields .
    """
    created = models.DateTimeField(auto_now_add=True,blank=False) #the time of creating the project
    title = models.CharField(max_length=100, blank=False, default='') # project title
    owner = models.ForeignKey('auth.User', related_name='owners', on_delete=models.CASCADE) # project owner
    group = models.OneToOneField(Group,on_delete=models.CASCADE,related_name='groups',blank=True,null=True)
    class Meta:
        # we order with the new one
        ordering = ('-created', )

    def __str__(self):
        return self.title



class Task(models.Model):
    """
    Task table here we create a relation ''
    """

    TODO = 'todo'
    DONE = 'done'
    INPROGRESS = 'in progress'

    CHOICES_STATUS = (
        (TODO, 'Todo'),
        (INPROGRESS, 'IN PROGRESS'),
        (DONE, 'Done')

    )

    title = models.CharField(max_length=100, blank=False, default='')
    project = models.ForeignKey('Project',related_name='tasks',on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User',related_name='owner',on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now=False,blank=True,null=True)
    end = models.DateTimeField(auto_now=False,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS)
    member = models.ManyToManyField(User,related_name='members',blank=True)
    def __str__(self):
        return self.title

class UserProfile(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   pic = models.ImageField(upload_to='upload/', blank=True, null=True)
