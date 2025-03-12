from django.contrib import admin
from .models import Project, Activity, Location, Status, Entry, UserProfile, ProjectHours

admin.site.register(Project)
admin.site.register(Activity)
admin.site.register(Location)
admin.site.register(Status)
admin.site.register(Entry)
admin.site.register(UserProfile)
admin.site.register(ProjectHours)
