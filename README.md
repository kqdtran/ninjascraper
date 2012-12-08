Ninja Scraper
=============
Get your exams from Ninja Course!

## Features and Acknowledgements
* Download all of the exams for the course you want into your local directory.
* Currently works for EVERY course that has its exams posted on Ninja Course. 
* Worked extremely well for CS courses thanks to Vaishaal Shankar. 
* Modified to work for every course by me, but you will need to know at least the professor's last name and the department's abbreviation to search for the exams (See guide below).

## Install
**You must have Python 2.6+ installed on your computer**. After that, just save the scrape_ninja.py (Python2) or scrape_ninja_py3k.py (Python 3) file to your local machine. 

**You will also need to install BeautifulSoup4**. The below commands should help you set up everything if you are on a Debian/Ubuntu machine. Windows and MacOSX users can find something very similar to these (see below).

#### If Python2 is the default version of Python on your machine and you want to use Python 2

* Set up easy_install (if it's not there already)
```
sudo apt-get install python-setuptools
```

* Then install BeautifulSoup4 by typing:
```
easy_install beautifulsoup4
```

(You can also follow the guide below for Py3k, just replace Python3 with Python2 or Python)

Yup! You are good to go. **Mac OSX** users can find a very similar guide here: http://stackoverflow.com/questions/452283/how-can-i-install-the-beautiful-soup-module-on-the-mac. Similarly, for **Windows users**, this may help: http://www.stat.ucla.edu/~rosario/classes/07F/202a/python/index.html.

#### If Python3 is the default version of Python on your machine, or Python2 is default BUT you want to use Python3

Note: I don't think setuptools is supported for Py3k, but instead they release something called Distribute. I don't know how to use it yet so you have to stick with me through this long installation guide (not that long :p)

* First, go to BS4's Website: http://www.crummy.com/software/BeautifulSoup/bs4/download/ and download the tarball of the latest version.
* Unpack the package by right click on it and 'Extract Here'. If you want to do it via command line, I think
```
tar -zxvf beautifulsoup4-4.1.3.tar.gz	 
```
 should do it. Replace the version's name in the tar file according to the version you downloaded.
* cd into the directory that BS4 unpacked into. Do a 'ls' to make sure setup.py is there. Then, on the terminal, type
```
sudo python3 setup.py install
```

At this point, you should have BeautifulSoup4 installed on your machine. TIME TO GET THE EXAMS.

## Usage: For CS Courses only
Please scroll down and read the heading below if you are not here for CS's Exams. By **CS**, I mean Computer Science, not Cognitive Science or Chicano Studies...

#### Python2

On the terminal, type  
```
python scrape_ninja.py 61C 
```
This will download all CS61C Exams from Ninja Course. Replace 61C with your CS class's course number to download the exams for that class. 

(You may want to add a '2.7' after python if you have multiple versions of Python installed)

#### Python3

On the terminal, type  
```
python3 scrape_ninja_py3k.py 61C 
```
Same effect as above. 

## Usage: For All other Subjects
*Note*: You will need to find the Department's Abbreviation Name, Ninja Course's Abbreviation for the Department, and your Professor's Last Name for this to work. It does sound like a lot of work, but trust me, it's relatively simple if you follow the guide below or have used Ninja Course to build your schedule before. 

So what do you need to do? Good question.

* First, find the Department's Abbreviation Name by going to Ninja Course (http://ninjacourses.com/explore/1/). Those words in CAPITAL is what you need. Write them down. I'll call this [DEPARTMENT ABBV] for future reference.

**Update**: Also, please note that there should be no space between the Department's Abbreviation. For example, if the department is MEC ENG (Mechanical Engineering), please type without space MECENG. 

![Department's Abbreviation](https://raw.github.com/kqdtran/ninjascraper/master/img/department_abbr.png)

* Next, you need to know Ninja Course's Abbreviation for the Department. More than often, it's the same as above, for example, Business Admin = UGBA, or Math = MATH, for both cases. You may need to guess the abbreviation Ninja Course uses to store the exams so it may be a little annoying in this step. I'll name this [NINJA ABBV]. 

**Update**: I've found that Ninja's Abbv is usually a combination of the initial of every word in the department's name. For example, Mechanical Engineering's Ninja Abbv would simply be ME, or Civil and Environmental Engineering would be CEE.  

* You will also need the course number. ECON 100A's course number will be simply 100A. Please don't forget letter like 'C' for cross-listed or 'AC' for American Culture. In other words, it's the class you want to download the exams for. [COURSE NUMBER]

* Finally, you need to know the last name of the instructor(s) whose exams you want to download. Just go to the Ratings tab like what most of us usually do before our Telebear appointment xD to look up their last names. This will be called [PROF LAST NAME].

![Ninja Course's Abbreviation](https://raw.github.com/kqdtran/ninjascraper/master/img/lastname.png)

Good, you are done! Time to open the terminal and get your exams! Navigate to the folder where you saved ninja_scraper.py or ninja_scraper_py3k.py in.

The syntax will be
```
python scrape_ninja.py [DEPARTMENT ABBV] [NINJA ABBV] [COURSE NUMBER] [PROF LAST NAME]
or
python3 scrape_ninja_py3k.py [DEPARTMENT ABBV] [NINJA ABBV] [COURSE NUMBER] [PROF LAST NAME]
```

For example, if I want to get ECON 100B's exams, in the ECON department, which is taught by Professor Wood, I would type
```
python scrape_ninja.py ECON ECON 100B Wood
or
python3 scrape_ninja_py3k.py ECON ECON 100B Wood
```

The result (for the above example):
![Result1](https://raw.github.com/kqdtran/ninjascraper/master/img/result1.png)


![Result2](https://raw.github.com/kqdtran/ninjascraper/master/img/result2.png)

Simple? Don't let the long description scared you. GO GET YOUR EXAMS AND ACE THE FINAL!

### FAQs
Q: Why don't you write something automatically get exams for us without too many additional arguments like what Vaishaal did for CS?

A: I would love to, but I need to study for my finals next week too... Beside, I don't really know how to do it at the moment. I will try to look into that when I can!

Q: Can I run this with Python3?

A: Yup! Python3 is fully supported. (Or at least I tested with both 2k and 3k on my local machine and they all worked fine...)

Q: This is so cool! Thanks!

A: You're welcome :) Please say thanks to Vaishaal Shankar. He did almost everything. I basically just tweaked it a little bit to work for other department's courses, added in this big README file to make it clearer. 


### Original Description by Vaishaal Shankar
https://github.com/Vaishaal/ninjascraper

gets exams from ninjacourses

Super duper beta!

only works for cs courses atm :P, and only works for finals.
defaults to cs70. Downloads pdf files to local directory.
Usage: (This will download all 61c final exams from ninjacourses)
```
python scrape_ninja.py 61C 
```
