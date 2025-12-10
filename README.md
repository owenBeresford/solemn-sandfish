

## DELIVERABLE (stage 1): [TICK]

This is a nano app, that I am assembling in Django, until other aspects of this 
problem are more mature.  A future version may be ReactNative and offline after 
installation, or something similar.

This needs form posts as the data is stored in a smol DB for ease of maintenance.
  The DB is expected to be small enough that it could be installed on the phone 
 (assuming I can find a SQLlite ReactNative module).

The user interactions should be fine on a variety of screen sizes.  They will 
work for mobile touch and mouse.   A keyboard based classic user should 
be fine, but I would like to review on a screen reader as I /use/ CSS.   
Currently a keyboard based hacker can bypass the error catching, and this leads
 to boring errors that expose nothing interesting.
I have ran interactions on non-latin1 text, and it just works.  I ought to add a 
test word of mandarin to the DB.   

I think this problem today is too small for an SPA.  It doesn't require real-
time updates.   For small and isolated codebases, React in particular is 
bloatware, and across time is an un-ending source of security problems.   If 
this grew to something like Grammarly or ProWritingAid, then an SPA such as 
React would be a good move.

I believe in writing to the scale of NOW and keeping budget available for later.
If this very much MVP was hosted on AWS Lanbda, it could support a parallel users
up something like 10/s or 1,000/min with zero effort beyond finishing it.
I would expect 80% of traffic to be in hot periods that account for 5-10% of a 
week.

# UPDATE Dec 2025: project folded [FROZEN]
All the earlier commits where on the same day (Aug 21st).
After a several month gap, the other stakeholder is withdrawing, so I am closing 
this project down. 


##  DELIVERABLE (stage 2): [DASH]

*Some* of the following:
- a slightly larger real SPA app, so it resembles the existing vendors better
    I'm thinking about Webcomponents for this to keep the code volume down
- an app deployed to app stores, offering the same interactions as this fast 
	demo
- a REST API to do translations in bulk.  Not sure about utility of this unless 
	the audience includes a large-scale XML system
- a large PDF *with interactions*
    The interactions may make this not possible, like interstitials or popup windows in the PDF doc
- direct retail of the DB to a vendor with similar services 

NOTICE: Stage2 requires that the database is complete.  This is not waiting on me.


### Docs for manual steps

[like npm packages.json steps, but needs to happen after you have a dev Python installed]
All these commands assume you are in the project root, and can be added to an IDE if you wished.

Tools can be handled easier if the project base_directory is in the PYTHON_PATH.   You could do the following (not sure about this step, as its not production code):
   pwd > $(python -m site --user-site)/verbs.pth

- install: pip install -r requirements.txt
- install-build: pip install -r requirements-dev.txt 
   - aka verbs-dev in Linux package naming schemes
- build: # this is python, nil
   - for a large scale service, I would apply a byte code optimiser, but out-of-scope.
- headers: stubgen --include-docstrings $FILES -o ./
   - if code is changed a noticeable amount, it may be wise to do this step to spot link/import errors faster
- lint: isort --profile black verbs/; black verbs/; pylint --recursive=y .
- test: python verbs/test/  
- run: python verbs/main.py runserver 
- docs: # today, please read the readme.md below here #TODO


### LIMITATIONS:

- Need to get a finished DB before adding more features
- Need to rebuild CSS as proper module
- Need to add web furniture like a favico
- Need to review the CSS/HTML5 form controls on a variety of phones
- Why doesn't Django router support branching on HTTP VERB?  My Controller is 
	more messy than it should be. 
    Try djangorestframework  https://www.freecodecamp.org/news/how-to-build-a-rest-api-in-django/
    https://python-rest-framework.readthedocs.io/en/latest/reference/controller.html


### FURTHER FEATURES (basic)

- Support punctuation is responses
- Dictionaries for further languages


### MAINTENANCE for stage1

- A better server-side router if this code is kept (using JS terminology)
- Possibly move service.py to REST API, but code is too smol to-date
- Make CSS more readable and a module
- Add web furniture
- Currently only 1 JS function and no JS frameworks used.  If more features via
	 JS are added, add a framework
- I am trying to have conservative choices to reduce code rot (see earlier 
	data files from 2y ago)


