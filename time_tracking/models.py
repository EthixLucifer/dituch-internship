from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    seconds_paused = models.PositiveIntegerField(default=0)
    pause_time = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    
    @property
    def hours(self):
        if self.end_time:
            return round((self.end_time - self.start_time).total_seconds() / 3600, 2)
        return None
    
    def __str__(self):
        return f"{self.user.username} - {self.project.name} ({self.start_time})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expected_hours_per_week = models.PositiveIntegerField(default=40)
    
    def __str__(self):
        return self.user.username

class ProjectHours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_hours = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.user.username} - {self.project.name}: {self.assigned_hours} hrs"
