#!/usr/bin/env python
import time
import os.path
from os.path import abspath, dirname, join
import sys
import datetime
import re
import random

DIR = dirname(abspath(dirname(__file__)))
sys.path.append(DIR)

from bugben import settings
from django.core.management import setup_environ

setup_environ(settings)

from mainsite.models import *
from django.contrib.auth.models import User


def main():
    create_admin()
    create_profile()


def create_admin():
    print "Creating user: admin"
    u = User.objects.create_user('admin', 'admin@admin.com', 'changeme')
    u.is_staff = True
    u.is_superuser = True
    u.save()

def create_profile(): 
    resume = Resume()
    resume.name = 'Ben Friedland'
    resume.phone = 'Please use email for initial contact'
    #TODO resume.email
    resume.url = 'http://www.bugben.com'
    resume.save()
    
    project = Project(name='Riker Ipsum')
    project.short_description = 'Generates text - like lorem ipsum - but uses real ' \
        'English. Taken from random samplings of dialog spoken by Commander ' \
        'William Riker in Star Trek: The Next Generation'
    project.long_description = '<p>Generates random text using real ' \
        'English - taken from random samplings of the entire catalog of ' \
        'dialog spoken by Commander William Riker in every episode of Star ' \
        'Trek: The Next Generation.</p>' \
        '<p>Useful for provisioning sample data to test a DB, or creating ' \
        'filler text for a design.</p>' \
        '<p>Since the entire catalog of dialog from every episode is ' \
        'included, endless possibilites of gibberish can be expected.</p>'
    project.deployment_url = 'http://ben174.github.io/rikeripsum/'
    project.src_url = 'https://github.com/ben174/rikeripsum'
    project.save()

    project = Project(name='MyTush')
    project.short_description = 'A utility to read map points from email ' \
        'attachments and push them to MyFord Touch / SYNC services.'
    project.long_description = '<p>The intent of this utility is to make ' \
        'it easy to send web points from a phone to MyFord Touch (Sync). ' \
        'Currently they have a crappy app that is supposed to do this ' \
        'called Sync Destinations. But it sucks. The map data it uses is ' \
        'bad and they should feel bad. This allows me to use my native ' \
        'Maps application and just share the point. I email it to an email ' \
        'address, and this script checks that mail address at a regular ' \
        'interval. When it sees a new message, it grabs the map point ' \
        '(VCF file), parses it, then sends it to the web service.</p>' \
        '<p>This utility:</p>' \
        '<ul>' \
        '<li>Checks email on the account</li>' \
        '<li>Looks for emails containing a VCF file.</li>' \
        '<li>Parses the VCF file for geographical data.</li>' \
        '<li>Sends that data to the MyFord Touch web service.</li>' \
        '<li>Deletes ALL MAIL from the mailbox.</li>' \
        '</ul>'
    project.deployment_url = None
    project.src_url = 'https://github.com/ben174/mytush'
    project.save()
    
    ProfileEntry.objects.create(entry='Senior software/systems engineer with twelve years of professional experience.')
    ProfileEntry.objects.create(entry='Unique mix of software engineering and systems administration.')
    ProfileEntry.objects.create(entry='Possess a wide range of technical knowledge in many areas, specializing in software architecture and development.')
    ProfileEntry.objects.create(entry='Extremely knowledgeable of the Linux operating system, along with various applications and tools commonly used in a Linux environment.')
    ProfileEntry.objects.create(entry='Twelve years of experience in the analysis, design and development of both commercial and custom software.')
    ProfileEntry.objects.create(entry='Red Hat Certified Engineer and Red Hat Certified Systems Administrator (Certification ID: 120-054-903)')
    ProfileEntry.objects.create(entry='Proficient in object design patterns, problem solving and identifying/avoiding anti-patterns.')
    ProfileEntry.objects.create(entry='Very strong analytical, oral, and written communication skills.')
    ProfileEntry.objects.create(entry='Contributor and supporter of various open source software projects.')



if __name__ == '__main__': 
    main()
