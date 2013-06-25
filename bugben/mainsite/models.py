from django.db import models
from django.db.models import signals
from django.contrib.auth.management import create_superuser
from django.contrib.auth import models as auth_app


# Prevent interactive question about wanting a superuser created.
signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_app,
    dispatch_uid = "django.contrib.auth.management.create_superuser"
)

class Project(models.Model): 
    """A class to hold a project. A project may be an application I've written, 
    a website I've created. Anything I'd like to show off.

    """

    name = models.CharField(
        max_length=200,
        unique=True,
        help_text = 'The name of this project.',
        blank=False,
    )

    short_description = models.CharField(
        max_length=200,
        help_text = 'Short description of the project.',
        blank=False,
    )

    long_description = models.TextField(
        help_text = 'Long description of the project.',
        blank=False,
    )

    deployment_url = models.URLField(
        help_text = 'URL of the deployed project (if a web app).',
        blank=True,
        null=True,
    )

    src_url = models.URLField(
        help_text = 'URL to source code of the project.',
        blank=True,
        null=True,
    )


class Resume(models.Model): 
    """Main details of my Resume.

    """

    name = models.CharField(
        max_length=100,
        help_text = 'My full name.',
        blank=False,
    )

    phone = models.CharField(
        max_length=100,
        help_text = 'My phone number.',
        blank=False,
    )

    url = models.CharField(
        max_length=100,
        help_text = 'My website address.',
        blank=False,
    )


class ImportantLink(models.Model): 
    """Main details of my Resume.

    """

    description = models.CharField(
        max_length=200,
        help_text = 'Description of the URL.',
        blank=False,
    )

    url = models.URLField(
        help_text = 'Address of this important URL.',
        blank=True,
        null=True,
    )


class ProfileEntry(models.Model): 
    entry = models.CharField(
        max_length=500,
        help_text = 'Entry in my profile.',
        blank=False,
    )


class ExpertiseEntry(models.Model): 
    entry = models.CharField(
        max_length=500,
        help_text = 'A section of expertise.',
        blank=False,
    )
    entry_details = models.TextField(
        help_text = 'Details on this expertise.',
        blank=False,
    )


class WorkHistoryEntry(models.Model): 
    client_name = models.CharField(
        max_length=200,
        help_text = 'The employer for whom I worked.',
        blank=False,
    )

    title = models.CharField(
        max_length=200,
        help_text = 'Title I held at this company.',
        blank=False,
    )

    contract = models.BooleanField(
        help_text = 'A flag indicating whether I was a contractor.',
        default=False, 
    )

    start_date = models.DateField(
        blank=True,
        null=True, 
    )

    end_date = models.DateField(
        blank=True,
        null=True, 
    )


class WorkAchievement(models.Model): 
    work_history_entry = models.ForeignKey(
        'WorkHistoryEntry',
        help_text = 'Work history entry to which this achievement belongs.',
    )

    achievement = models.TextField(
        help_text = 'A description of the achievement accomplished.',
        blank=False,
    )
