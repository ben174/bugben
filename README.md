Resume of Ben Friedland
=======================
<img align="right" src="https://raw.githubusercontent.com/ben174/bugben/master/logo.png">

#### http://www.bugben.com


### My career, as a git commit history.

I've tried a couple iterations at my resume, an XML persisted solution
way back in the 90's, a database persisted Django project
(https://github.com/ben174/bugben/tree/3.0), and now I'm trying to simplify
it by using a basic filesystem structure, with a git repository to
maintain version history.

Looking for the old Django Project? [Branch 3.0](https://github.com/ben174/bugben/tree/3.0)

### The Renderer

I've created a separate Python project renders this resume to various formats.
HTML, TXT, PDF, etc. The goal of this project is to create a standard format
for a Resume repository and this Renderer could be used and expanded on to
render your repo.

https://github.com/ben174/resume-renderer

The rendered output:

#### http://www.bugben.com


Directory Structure
--------------------------

The creation date of each subdirectory in the Git history represents the
start date in my lifetime (i.e. started the job, created the project, started
using the skill).

##### A pseudo `git-log`, a timeline of my career:
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

##### `NAME.txt`

A file containing a friendly name of this particular entry, e.g.: `Riker Ipsum`.
While the directory name should be indicative of what this entry represents,
the renderer uses this string to make a more friendly name to output on the
resume.

##### `README.md`

Contains the basic body detailing the entry itself. For experience, this
contains my job title, and some accomplishments. Keeping this in a `README.md`
is handy because GitHub will display this markdown when navigating the repo.

##### `LOGO.png`

A logo representing the entry (company logo, project logo). The renderer will
render this logo next to each entry.


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
the project.

    .gitmodules

    [submodule "src"]
        path = src
        url = https://github.com/ben174/bugben.git

##### `ORDER.txt`

Since some of my projects are more notable than others and I'd like to be
able to order them, the Projects directory has a `ORDER.txt` file which
contains the directory names in the order they should be rendered on my resume.

Expertise
---------

Fields of expertise go here as directories, e.g.: `Web Development`, `Operating
Systems`. Within each directory would be several files for each particular
skill, e.g.: `Python`, `HTML`. The creation date of this file determines when I 
first started using that skill. The renderer may use this to add weight to
individual skills based on the number of years I've used them. Optionally
some text within the file can describe where I've used it and how comfortable
I am with it.

#### `SUMMARY.md`

A simple markdown-formatted profile summary which is rendered at the top of my
resume. In my case, I like a concise bulleted list outlining some of my skills
and accomplishments.

#### `LINKS.md`

A simple markdown-formatted bulleted list of important links. Such as my Home
Page, LinkedIn profile, and GitHub page.

#### `EXPERTISE.json` (Deprecated)

~~A json structure~~ (This has been deprecated in favor of git commit history):

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

* I am currently employed

* I'm actively working on a project

* I've made some community contributions recently

