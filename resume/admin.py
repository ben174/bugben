from django.contrib import admin
from resume.models import *

admin.site.register([
    Resume,
    Project,
    ImportantLink,
    ProfileEntry,
    ExpertiseEntry,
    WorkHistoryEntry,
    WorkAchievement,
])
