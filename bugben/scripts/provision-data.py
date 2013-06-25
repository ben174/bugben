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


    entry = ExpertiseEntry(entry='Web Application Development')
    entry.entry_details = 'Python, Django, South, Front End Development (HTML5, jQuery, AJAX, Bootstrap), Internal Tools'

    entry = ExpertiseEntry(entry='Operating Systems')
    entry.entry_details = 'Linux (Red Hat Enterprise Linux (RHEL), Ubuntu, Debian, Fedora, CentOS), Sun Solaris, other Unix variants, OSX, Microsoft Windows'
    entry.save()

    entry = ExpertiseEntry(entry='Microsoft .NET')
    entry.entry_details = 'C#, Visual Basic .NET, Windows Forms, ASP.NET, WPF, WCF'
    entry.save()

    entry = ExpertiseEntry(entry='Other Languages')
    entry.entry_details = 'Python, ColdFusion, PHP, Perl'
    entry.save()

    entry = ExpertiseEntry(entry='Databases')
    entry.entry_details = 'MySQL, Microsoft SQL Server 2000-2008, Oracle: 8i - 9i - 10g, PostgreSQL'
    entry.save()

    entry = ExpertiseEntry(entry='Development Environments')
    entry.entry_details = 'VIM, Visual Studio .NET, Eclipse, NetBeans, Notepad'
    entry.save()

    entry = ExpertiseEntry(entry='Other Skills')
    entry.entry_details = 'XML, JSON, XSL, AJAX, JavaScript, HTML, HTML 5, XHTML, CSS, JQuery, Scriptaculous, ASP, VBScript, Bash (shell scripting), VIM, SQL, PL/SQL, T-SQL, ORM (Hibernate/NHibernate), GIT, Heroku, Amazon EC2, Apache, GIS, Reporting, Video/Audio Processing and Production'
    entry.save()


    work = WorkHistoryEntry(client_name='University of Southern California (USC)')
    work.location = 'Los Angeles, California'
    work.timespan = 'February, 2013 - Current'
    work.title = 'Software Developer - Consultant'
    work.save()
    achivement = WorkAchievement(description='Consultant for various jobs. Created a data warehouse application in Django with advanced reshaping of data. ')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='TiVo')
    work.location = 'Santa Clara, California'
    work.timespan = 'June, 2011 - Current'
    work.title = 'Senior Unix Engineer / Tools Developer'
    work.save()
    achivement = WorkAchievement(description='Heavy use of Django to create several internal tools, including an advanced scheduling tool used daily by the NOC team. This tool is capable of finding holes in the schedule, allowing users to request time off and allows managers to manage the schedule using a very slick UI. ')
    achivement.entry = work
    achivement.save()

    achivement = WorkAchievement(description='In a very short time, learned the vast workings of one of the most complex Linux environments in existence. TiVo pioneered using Linux as an appliance, and the workplace offered the opportunity to work with some of the greatest minds in the field.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Mixed heavy development talents with day-to-day operations within the NOC and was able to automate many tasks, saving several man-hours per day.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='MedicAlert Foundation')
    work.location = 'Turlock, California'
    work.timespan = 'November, 2008 - June, 2011'
    work.title = 'Senior Software Engineer'
    work.save()
    achivement = WorkAchievement(description='Honored employee - awarded recognition In April 2009. The only person in a 200+ employee company to be honored the entire year of 2009.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Assisted with migration from Sun Web Server to Apache. Wrote scripts to automatically migrate a huge list of redirects from Sun\'s XML redirect configuration to Apache\'s text based configuration.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Heavy use of JQuery and Ajax to create a personal health record editor for users of MedicAlert service. This replaced an old broken system and the company was extremely pleased to go from several dozens of customer complaints per day to virtually zero.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Developed a class library in .NET which acted as a transport for web service calls between a legacy VB6 app and newer web services.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='American Medical Response')
    work.location = 'Modesto, California'
    work.timespan = 'November, 2006 - November, 2008'
    work.title = 'Senior Software Engineer'
    work.save()
    achivement = WorkAchievement(description='Developed an automatic update client run on the field by hundreds of ambulance which would query a web service to determine if a newer version of software was available. If a new package was available it would queue up the download using Microsoft\'s Background Intelligent Transfer Service (BITS) API , which would trickle download the file based on limited internet availability on the field. When the download was complete, the tool would decrypt the archive and extract, then automatically restart the necessary modules. Every bit of this was done without any UI interaction - completely invisible to the user.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Created a very sophisticated console based daemon app which would monitor Tracy Fire Department\'s live data stream and send information to AMR\'s Ambulance dispatcher units through a six-step process of downloading, extracting, converting, processing, uploading, and logging. This data was emergency-service-critical and the daemon needed to be rock solid. It never once went down.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='MedicAlert Foundation')
    work.location = 'Turlock, California'
    work.timespan = 'January, 2006 - July, 2006'
    work.title = '.NET Engineer (Consultant)'
    work.save()
    achivement = WorkAchievement(description='Introduced and implemented object/relational persistence tools. Created entire class library, then used NHibernate to logically map all objects to existing database structure. Then created very simple CRUDs to allow edits through a .NET Web Service. ')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='Stanislaus County Superior Court')
    work.location = 'Modesto, California'
    work.timespan = 'July, 2004 - December, 2005'
    work.title = '.NET Engineer (Consultant)'
    work.save()
    achivement = WorkAchievement(description='Migrated database from Oracle to SQL Server. ')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Developed entire cashiering system from the ground up using C# and SQL Server. This included an expansion of their database schema and migration of portions of an old, undocumented Cobol application.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Created a ASP.NET web-based court calendar application to assist with the scheduling of court cases. This calendar has become a key component in their day-to-day operations and was featured in an article in the Modesto Bee.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='LowerMyBills.com')
    work.location = 'Santa Monica, California'
    work.timespan = 'November, 2003 - June, 2004'
    work.title = '.NET Engineer'
    work.save()
    achivement = WorkAchievement(description='Developed a front-end Windows Forms user interface for data entry of lenders. Also created an auto-updating component that would query an internal web server on each launch, looking for updates. If updates were available, it would update the application and restart the application, all transparent to the user. ')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Performed load testing for migrating an existing application from JRUN to Tomcat with clustering and load balancing.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Wrote an extensive logging framework for tracking and debugging issues within the enterprise applications.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='California CAD Solutions')
    work.location = 'Modesto, California'
    work.timespan = 'December, 2001 - October, 2003 / June, 1999 - January, 2000'
    work.title = 'Senior Programmer / Architect'
    work.save()
    achivement = WorkAchievement(description='Used advanced geometry to create a geocoding algorithm which was capable of guessing the geographic location of a street address. ')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Created a real-time hierarchical database tracer for tracing pipe networks upstream or downstream.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Developed a modular Web application framework backend in ColdFusion with a skinnable front-end.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Designed, architected, and programmed many GIS solutions on a variety of platforms including ColdFusion, ASP.NET (C#), and J2EE (Tomcat).')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Interfaced with many different database platforms including DB2, Oracle 8/9i, SQL Server, Microsoft Access, DBF, SHP, SDF, MySQL, and many more.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Performed advanced file I/O on the SHP binary file format. This included parsing header information and creating a separate index file containing file offset addresses of key data.')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Created T-SQL and PL/SQL stored procedures for nightly batch processing of geographical data.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='Therapeutic Research, Inc.')
    work.location = 'Stockton, California'
    work.timespan = 'October, 2000 - July, 2001'
    work.title = 'Contract Position: Application Developer / Database Architect'
    work.save()
    achivement = WorkAchievement(description='Developed a secure authentication system for subscribers to an e-zine. (ASP 3.0) ')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Migrated a database of over 100,000 subscribers to a normalized database in SQL Server 2000.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='Admail West')
    work.location = 'Sacramento, California'
    work.timespan = 'June, 2000 - October, 2000'
    work.title = 'Team Leader, Intranet Application Development'
    work.save()
    achivement = WorkAchievement(description='Managed a team of four developers in the creation of an intranet application for data entry. This included a rich front-end - heavy in JavaScript/DHTML, and a powerful back-end in ColdFusion.  ')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Developed a database logging system which would track the speed and accuracy of individual data entry clerks.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='KeraVision, Inc.')
    work.location = 'San Rafael, California'
    work.timespan = 'June, 2000'
    work.title = 'Contract Position: ColdFusion Developer'
    work.save()
    achivement = WorkAchievement(description='Performed maintenance on a high-traffic web site to decrease load times. ')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Optimized back-end ColdFusion code to decrease server impact during peak traffic.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='marchFIRST, Inc.')
    work.location = 'San Francisco, California'
    work.timespan = 'January, 2000 - June, 2000'
    work.title = 'ColdFusion Developer'
    work.save()
    achivement = WorkAchievement(description='Created dynamic front-end pages for large sites such as Pottery Barn, Williams-Sonoma, and Toys 'R' Us. ')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Lead a team of six engineers for the entire front-end development of Williams-Sonoma Online Wedding Registry.')
    achivement.entry = work
    achivement.save()

    work = WorkHistoryEntry(client_name='Big Valley Internet')
    work.location = 'Ceres, California'
    work.timespan = 'April, 1998 - June, 1999'
    work.title = 'Webmaster'
    work.save()
    achivement = WorkAchievement(description='Created an online telephone prefix lookup to find local numbers for a large ISP. ')
    achivement.entry = work
    achivement.save()
    achivement = WorkAchievement(description='Used ColdFusion to create dynamic Web applications for several clients.')
    achivement.entry = work
    achivement.save()



if __name__ == '__main__': 
    main()
