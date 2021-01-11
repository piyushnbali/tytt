from django.db import models

class timetable(models.Model):
     Subject = models.CharField(max_length=50,null=False)
     Day = models.CharField(max_length=50)
     start_time_min = models.IntegerField()
     end_time_min = models.IntegerField()


class students(models.Model):
    roll_no = models.CharField(max_length=50,null=False)
    Subject = models.CharField(max_length=50,null=False)

class subject_link(models.Model):
    Subject = models.CharField(unique=True,max_length=50,null=False)
    link = models.CharField(max_length=5500)
