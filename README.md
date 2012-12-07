### Ninja Scraper
Gets your exams from Ninja Course!

## Features
* Currently worked for EVERY course that has potential exams. 
* Worked extremely well for CS courses thanks to Vaishall Shankar. 
* Modified to work for every course by me, but you need to know at least your professor's last name and the department's abbreviation to search for the exams.

## Install
You must have Python 2 on your computer (2.7 preferred). After that, just save the scrape_ninja.py file to your local machine.

## Usage: For CS Courses only
Please scroll down and read the heading below if you are not here for CS's Exams. By 'CS', I mean Computer Science, not Cognitive Science or Chicano Studies...

On the terminal, type  
```
python scrape_ninja.py 61C 
```
This will download all 61C Exams from NinjaCourses. Replace 61C with your *CS*'s course number to download the exams for that course. 

(You may want to add a '2.7' after python if you have multiple versions of Python installed)

## Usage: For All other Subjects
*Note*: You will need to find the Department's Abbreviation Name, Ninja Course's Abbreviation for the Department, and your Professor's Last Name for this to work. It does sound like a lot of work, but trust me, it's relatively simple if you follow the guide below.

So what do you need to do? Good question.

* First, find the Department's Abbreviation Name by going to Ninja Course (http://ninjacourses.com/explore/1/). 
![Department's Abbreviation](/img/department_abbr.png)

### Original Description by Vaishall Shankar
https://github.com/Vaishaal/ninjascraper

gets exams from ninjacourses

Super duper beta!

only works for cs courses atm :P, and only works for finals.
defaults to cs70. Downloads pdf files to local directory.
Usage: (This will download all 61c final exams from ninjacourses)
```
python scrape_ninja.py 61C 
```
