from django.contrib import admin
from resume.models import Resume, Project, ImportantLink, ProfileEntry, ExpertiseEntry, WorkHistoryEntry, WorkAchievement


admin.site.register([
    Resume,
    Project,
    ImportantLink,
    ProfileEntry,
    ExpertiseEntry,
    WorkHistoryEntry,
    WorkAchievement,
])
