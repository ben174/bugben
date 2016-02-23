bugben.com
==========

### My resume, as a git repository.

I've tried a couple iterations at my resume, an XML persisted solution
way back in the 90's, a database persisted Django project
(https://github.com/ben174/bugben/tree/3.0), and now I'm trying to simplify
it by using a basic filesystem structure, with a git repository to
maintain version history.

Directory Structure
===================

Each directory contains a README.md with a basic body of text detailing itself.
It can optionally have a LOGO.png which will represent it when it is rendered.
Individual entries are committed within as subdirectories.  The creation date
of each subdirectory in the Git history represents the start date in my
lifetime (i.e. started the job, created the project).

A directory can optionally contain an ORDER.txt which contains a listing of
directory names, in the order they should be sorted. If this is left out,
the renderer will sort the directories by the date they were committed.


Experience
----------

Each directory in here is a single position I've held. The date the directory
was created is the start date of the position. A single file titled DEPARTURE
is committed on my end date at that company. It can optionally contain some
text with details on the DEPARTURE. e.g.: Fired for stealing stationary.


Projects
--------

Open source community contributions go here as directories. They can
optionally contain a 'src' submodule which links to the repo which hosts
the project. A README.md details the project and can link to its hosted site.

    .gitmodules

    [submodule "src"]
        path = src
        url = https://github.com/ben174/bugben.git

Again, the creation date of the directory determines when the project was
created.

Since some of my projects are more notable than others and I'd like to be
able to order them, the Projects directory has a order.txt file which
contains the directory names in the order they should be rendered on my resume.

SUMMARY.md
----------
A simple markdown-formatted bulleted list of my primary skills. Rendered at the
top of the resume.

LINKS.md
----------
A simple markdown-formatted bulleted list of important links. Such as my Home
Page, LinkedIn profile, and GitHub page.

EXPERTISE.json
--------------

A json structure:

```javascript
[
  {
    "category": "Web Application Development",
    "entries": [
      {
        "title": "Python"
        "years": 5,
      },
      {
        "title": "Django"
        "years": 4,
      }
    ]
  },
  {
    "category": "Databases",
    "entries": [
      {
        "title": "MySql"
        "years": 5,
      },
      {
        "title": "PostgreSQL"
        "years": 4,
      }
    ]
  }
]
```
