from django.db import models


class Member(models.Model):
    project_topic = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=60)
    short_info = models.TextField(null = True, blank = True)
    #participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    # host=
    topic = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
