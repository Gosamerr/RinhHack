from django.db import models


class Members(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=60)
    short_info = models.CharField(max_length=150)

    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name

    def full_info(self):
        info_full =  self.name + " " + self.surname + " " + self.short_info + " " + self.pub_date
        return info_full

class Project(models.Model):
    members = models.ForeignKey(Members, on_delete=models.CASCADE)
    WAY_OF_PROJECTS = {
        'KS':"Кибербезопасность",
        'IP':"Импортозамещение в программном обеспечении",
        'BD&II':"Большие данные и искусственный интеллект",
    }
    way = models.CharField(max_length=5, choices=WAY_OF_PROJECTS)
    topic = models.CharField(max_length=200)

    workbar = models.IntegerField(default=0)
    def __str__(self):
        return self.way