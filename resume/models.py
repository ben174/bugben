from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    """A class to hold a project. A project may be an application I've written,
    a website I've created. Anything I'd like to show off.

    """

    name = models.CharField(
        max_length=200,
        unique=True,
        help_text='The name of this project.',
        blank=False,
    )

    short_description = models.CharField(
        max_length=200,
        help_text='Short description of the project.',
        blank=False,
    )

    long_description = models.TextField(
        help_text='Long description of the project.',
        blank=False,
    )

    deployment_url = models.URLField(
        help_text='URL of the deployed project (if a web app).',
        blank=True,
        null=True,
    )

    src_url = models.URLField(
        help_text='URL to source code of the project.',
        blank=True,
        null=True,
    )

    sort_order = models.FloatField(
        default=10,
        help_text='Order in which this entry is displayed.',
        blank=False,
        null=False,
    )

    resume = models.ForeignKey(
        'Resume',
        on_delete=models.CASCADE,
    )

    @property
    def logo_path(self):
        return 'img/logos/{}.png'.format(slugify(self.name))

    def __str__(self):
        return "Project: %s" % self.name

    class Meta:
        ordering = ['sort_order']


class Resume(models.Model):
    """Main details of my Resume.

    """

    name = models.CharField(
        max_length=100,
        help_text='My full name.',
        blank=False,
    )

    phone = models.CharField(
        max_length=100,
        help_text='My phone number.',
        blank=False,
    )

    email = models.CharField(
        max_length=100,
        help_text='My email address.',
        blank=False,
    )

    url = models.CharField(
        max_length=100,
        help_text='My website address.',
        blank=False,
    )

    sort_order = models.FloatField(
        default=10,
        help_text='Order in which this entry is displayed.',
        blank=False,
        null=False,
    )

    def __str__(self):
        return "Resume: %s" % self.name

    class Meta:
        ordering = ['sort_order']


class ImportantLink(models.Model):
    """Links which are important to my profile.

    """

    description = models.CharField(
        max_length=200,
        help_text='Description of the URL.',
        blank=False,
    )

    url = models.URLField(
        help_text='Address of this important URL.',
        blank=True,
        null=True,
    )

    sort_order = models.FloatField(
        default=10,
        help_text='Order in which this entry is displayed.',
        blank=False,
        null=False,
    )

    resume = models.ForeignKey(
        'Resume',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['sort_order']


class ProfileEntry(models.Model):
    entry = models.CharField(
        max_length=500,
        help_text='Entry in my profile.',
        blank=False,
    )

    sort_order = models.FloatField(
        default=10,
        help_text='Order in which this entry is displayed.',
        blank=False,
        null=False,
    )

    resume = models.ForeignKey(
        'Resume',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return 'Profile: %s' % self.entry

    class Meta:
        ordering = ['sort_order']


class ExpertiseEntry(models.Model):
    entry = models.CharField(
        max_length=500,
        help_text='A section of expertise.',
        blank=False,
    )

    entry_details = models.TextField(
        help_text='Details on this expertise.',
        blank=False,
    )

    sort_order = models.FloatField(
        default=10,
        help_text='Order in which this entry is displayed.',
        blank=False,
        null=False,
    )

    resume = models.ForeignKey(
        'Resume',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return 'Expertise: %s' % self.entry

    class Meta:
        ordering = ['sort_order']


class WorkHistoryEntry(models.Model):
    client_name = models.CharField(
        max_length=200,
        help_text='The employer for whom I worked.',
        blank=False,
    )

    title = models.CharField(
        max_length=200,
        help_text='Title I held at this company.',
        blank=False,
    )

    location = models.CharField(
        max_length=200,
        help_text='Location in which the company is located.',
        blank=False,
    )

    contract = models.BooleanField(
        help_text='A flag indicating whether I was a contractor.',
        default=False,
    )

    timespan = models.CharField(
        max_length=200,
        help_text='Timespan in which I worked at the company.',
        blank=False,
    )

    sort_order = models.FloatField(
        default=10,
        help_text='Order in which this entry is displayed.',
        blank=False,
        null=False,
    )

    resume = models.ForeignKey(
        'Resume',
        on_delete=models.CASCADE,
    )

    @property
    def logo_path(self):
        return 'img/logos/{}.png'.format(slugify(self.client_name))

    def __str__(self):
        return 'Work History: %s' % self.client_name

    class Meta:
        ordering = ['sort_order']



class WorkAchievement(models.Model):
    entry = models.ForeignKey(
        'WorkHistoryEntry',
        help_text='Work history entry to which this achievement belongs.',
        on_delete=models.CASCADE,
    )

    description = models.TextField(
        help_text='A description of the achievement accomplished.',
        blank=False,
    )

    sort_order = models.FloatField(
        default=10,
        help_text='Order in which this entry is displayed.',
        blank=False,
        null=False,
    )

    def __str__(self):
        client = self.entry.client_name
        short_desc = self.description[0:50]
        return 'Achievement (%s): %s' % (client, short_desc)

    class Meta:
        ordering = ['sort_order']
