from datetime import datetime

import datetime
def get_entry(category, filename, name, years, body=None):
    date = datetime.datetime.now() - datetime.timedelta(days=365*years)
    gitdate = datetime_to_git_string(date)
    path = '{}/{}'.format(category, filename)
    with open(path, 'w') as f:
        f.write(name)
        f.flush()
        f.close()
    print 'git add {}'.format(path)
    print 'GIT_AUTHOR_DATE="{}" GIT_COMMITTER_DATE="{}" git commit {} -m \"Started using {}\"'.format(gitdate, gitdate, path, name)


def datetime_to_git_string(dt):
    return datetime.datetime.strftime(dt, '%a %b %d %H:%M:%S %Y +0800')

#print get_entry('webapp', 'django-rest-framework', 'Django Rest Framework', 2)
#print get_entry('webapp', 'django', 'Django', 5)
get_entry('webapp', 'python', 'Python', 5)
get_entry('webapp', 'flask', 'Flask', 2)
get_entry('webapp', 'front-end', 'Front End Development', 17)
get_entry('webapp', 'html', 'HTML/HTML5', 15)
get_entry('webapp', 'javascript', 'JavaScript/ES6', 15)
get_entry('webapp', 'angular', 'Angular', 2)
get_entry('webapp', 'jquery', 'jQuery', 5)
get_entry('webapp', 'ajax', 'AJAX', 5)
get_entry('webapp', 'bootstrap', 'Bootstrap 3', 2)
get_entry('webapp', 'websockets', 'Web Sockets', 1)
