Resume of Ben Friedland
=======================

#### http://www.bugben.com

![Resume Thumbnail][logo]

[logo]: https://raw.githubusercontent.com/ben174/bugben/master/logo.png "Resume of Ben Friedland"


### My resume, as a git repository.

I've tried a couple iterations at my resume, an XML persisted solution
way back in the 90's, a database persisted Django project
(https://github.com/ben174/bugben/tree/3.0), and now I'm trying to simplify
it by using a basic filesystem structure, with a git repository to
maintain version history.


### The Renderer

I've created a separate Python project renders this resume to various formats.
HTML, TXT, PDF, etc. The goal of this project is to create a standard format
for a Resume repository and this Renderer could be used and expanded on to
render your repo.

https://github.com/ben174/resume-renderer

The rendered output:

#### http://www.bugben.com


Resume Directory Structure
==========================

The creation date of each subdirectory in the Git history represents the
start date in my lifetime (i.e. started the job, created the project, started
using the skill).

#### A pseudo `git-log`, a timeline of my carrer.
```
*   08aeead Started working at 'Clutter'
|\  
| * 15e6b24 Began using Django
| * 96e1c27 Began using Angular
| *   45dc382 Started Project 'ShowerTexts'
| |\  
| |/  
|/|   
* | 86d8344 Started working at 'Shape Security'
* | 5ecbe26 Began using 'Selenium'
* | 3792057 Began using 'ReactJS'
| * b34098c Started Project 'Rick Roulette'
|/

```


#### File structure

Each subdirectory contains files detailing itself.

##### `README.md`

Each directory contains a `README.md` with a basic body of text detailing itself.
This is handy because GitHub will display this markdown when navigating the repo.

##### `LOGO.png`

A logo representing the entry (company logo, project logo). The renderer will
render this logo next to each entry.

##### `ORDER.txt`

A directory can optionally contain an `ORDER.txt` which contains a listing of
directory names, in the order they should be sorted. If this is left out,
the renderer will sort the directories by the date they were committed.


Experience
----------

Each directory in here is a single position I've held. The date the directory
was created is the start date of the position. A single file titled `DEPARTURE`
is committed on my end date at that company. It can optionally contain some
text with details on the departure, e.g.: `Fired for stealing stationary`.


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

Expertise
---------

Fields of expertise go here as directories. Within each directory would be a
particular skill as an individual file, e.g.: `Python`, `HTML`. The creation
date of this file determines when I first started using that skill. Optionally
some text within the file can describe where I've used it and how comfortable
I am with it.

#### `SUMMARY.md`

A simple markdown-formatted bulleted list of my primary skills. Rendered at the
top of the resume.

#### `LINKS.md`

A simple markdown-formatted bulleted list of important links. Such as my Home
Page, LinkedIn profile, and GitHub page.

#### `EXPERTISE.json` (Deprecated)

~A json structure~ (This has been deprecated in favor of git commit history):

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

### Tests

Tests will assert that:

* I have a job

* I'm actively working on a project

* I've made some community contributions in the past week

