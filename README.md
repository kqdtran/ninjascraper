#### Ninja Scraper
Gets your exams from Ninja Course!

## Features and Descriptions
* Download all the exams for the course you want into your local directory.
* Currently works for EVERY course that has its exams posted. 
* Worked extremely well for CS courses thanks to Vaishaal Shankar. 
* Modified to work for every course by me, but you need to know at least your professor's last name and the department's abbreviation to search for the exams.

## Install
You must have Python 2 on your computer (2.7 preferred). After that, just save the scrape_ninja.py file to your local machine.

## Usage: For CS Courses only
Please scroll down and read the heading below if you are not here for CS's Exams. By 'CS', I mean Computer Science, not Cognitive Science or Chicano Studies...

On the terminal, type  
```python
python scrape_ninja.py 61C 
```
This will download all 61C Exams from NinjaCourses. Replace 61C with your *CS*'s course number to download the exams for that course. 

(You may want to add a '2.7' after python if you have multiple versions of Python installed)

## Usage: For All other Subjects
*Note*: You will need to find the Department's Abbreviation Name, Ninja Course's Abbreviation for the Department, and your Professor's Last Name for this to work. It does sound like a lot of work, but trust me, it's relatively simple if you follow the guide below.

So what do you need to do? Good question.

* First, find the Department's Abbreviation Name by going to Ninja Course (http://ninjacourses.com/explore/1/). Those words in CAPITAL is what you need. Write them down. I'll call this [DEPARTMENT ABBV] for future reference.
![Department's Abbreviation](https://raw.github.com/kqdtran/ninjascraper/master/img/department_abbr.png)

* Next, you need to know Ninja Course's Abbreviation for the Department. More than often, it's the same as above, for example, Business Admin = UGBA, or Math = MATH, for both cases. You may need to guess the abbreviation Ninja Course uses to store the exams so it may be a little annoying in this step. I'll name this [NINJA ABBV]. 

* You will also need the course number. ECON 100A's course number will be simply 100A. In other words, it's the class you want to download the exams for. [COURSE NUMBER]

* Finally, you need to know the last name of the instructor(s) whose exams you want to download. Just go to the Ratings tab like what most of us usually do before our Telebear appointment xD. This will be called [PROF LAST NAME].
![Ninja Course's Abbreviation](https://raw.github.com/kqdtran/ninjascraper/master/img/lastname.png)

Good, you are done! Time to open the terminal and get your exams! Navigate to the folder where you saved ninja_scraper.py in.

The syntax will be
```python
python scrape_ninja.py [DEPARTMENT ABBV] [NINJA ABBV] [COURSE NUMBER] [PROF LAST NAME]
```

For example, if I want to get ECON 100B's exams, in the ECON department, which is taught by Professor Wood, I would type
```python
python scrape_ninja.py ECON ECON 100B Wood
```

Simple? Don't let the long description scared you. GO GET YOUR EXAMS AND STUDY!

### FAQs
Q: Why don't you write something automatically get exams for us without too many additional arguments like what Vaishall did for CS?

A: I would love to, but we have finals next week... Beside, I'm inexperienced so that may take a lot of time. I will do that whenever I can!

Q: Can I run this with Python3?

A: Currently, no. Python3's urllib.request is pretty annoying and will require a lot of syntax's editting.

Q: This is so cool! Thanks!

A: You're welcome :) Please thanks Vaishaal Shankar as well. He did almost everything. I basically just tweaked it a little bit, added in this big README file to make it clearer and support all other courses beside CS courses. 


### Original Description by Vaishaal Shankar
https://github.com/Vaishaal/ninjascraper

gets exams from ninjacourses

Super duper beta!

only works for cs courses atm :P, and only works for finals.
defaults to cs70. Downloads pdf files to local directory.
Usage: (This will download all 61c final exams from ninjacourses)
```python
python scrape_ninja.py 61C 
```
