from django.contrib import admin
from mainsite.models import *

admin.site.register([
    Project,
    Resume,
    WorkHistoryEntry,
    WorkAchievement,
    ImportantLink,
    ProfileEntry,
    ExpertiseEntry,
])
