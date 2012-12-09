Ninja Scraper
=============
Get your exams from Ninja Course!

## Versions and Changelog
* **v1.2**(12/8/2012): Modified to take one less command-line argumment, aka no need for professor's name anymore! It will now scrape through all exams belong to professors whose names are on the Ratings tab. Also, the exams will be saved in a directory named after the course whose exams you want to search for.
* **v1.1**(12/7/2012): Modified to work with every department, but users still need the abbreviations and professor's name. Also added support for Python3
* **v1.0**(12/6/2012): Forked from https://github.com/Vaishaal/ninjascraper

## Features and Acknowledgements
* Download all of the exams for the course you want into your local directory.
* Currently work for EVERY course that has its exams posted on Ninja Course. 
* Worked extremely well for CS courses thanks to Vaishaal Shankar. 
* Modified to work for every course by me, but you will need to know the department's abbreviation to search for the exams (See guide below).
* There is a very, very tiny bug in v1.2. A couple of courses have exams belong to professors that are not on NinjaCourse. For example, CS174 has 4 exams belong to Prof. Bartlett, but as you can see, he doesn't have an entry on NC http://ninjacourses.com/explore/1/course/COMPSCI/174/#ratings so the scraper couldn't find him. I have yet to find a solution to this problem, but I'll try to look into it soon.

## Installation
**You must have Python 2.6+ installed on your computer**. After that, just save the scrape_ninja.py (Python2) or scrape_ninja_py3k.py (Python 3) file to your local machine. 

**You will also need to install BeautifulSoup4**. The below commands should help you set up everything if you are on a Debian/Ubuntu machine. Windows and MacOSX users can find something very similar to these (see below).

#### If Python2 is the default version of Python on your machine and you want to use Python2

* Set up easy_install (if it's not there already)
```
sudo apt-get install python-setuptools
```

* Then install BeautifulSoup4 by typing:
```
easy_install beautifulsoup4
```

(You can also follow the guide below for Py3k, just replace Python3 with Python2 or Python)

Yup! You are good to go. **Mac OSX users** can find a very similar guide here: http://stackoverflow.com/questions/452283/how-can-i-install-the-beautiful-soup-module-on-the-mac. Similarly, for **Windows users**, this may help: http://www.stat.ucla.edu/~rosario/classes/07F/202a/python/index.html.

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
which will yield the same effect as above. 

## Usage: For All other Subjects
*Note*: You will need to find the Department's Abbreviation Name and Ninja Course's Abbreviation for the Department for this to work. It does sound like a lot of work, but trust me, it's relatively simple if you follow the guide below or have used Ninja Course to build your schedule before. 

So what do you need to do? Good question.

* First, find the Department's Abbreviation Name by going to Ninja Course (http://ninjacourses.com/explore/1/). Those words in CAPITAL are what you need. Write them down. I'll call this **[DEPARTMENT ABBV]** for future reference. Please note that there should be no space between the Department's Abbreviation. For example, if the department is MEC ENG (Mechanical Engineering), please type without space MECENG. 

![Department's Abbreviation](https://raw.github.com/kqdtran/ninjascraper/master/img/department_abbr.png)

* Next, you need to know Ninja Course's Abbreviation for the Department. More than often, it's the same as above, for example, Business Admin = UGBA, or Math = MATH, for both cases. You may need to guess the abbreviation Ninja Course uses to store the exams so it may be a little annoying. I'll call this **[NINJA ABBV]** for later use. It is also common for the Ninja's ABBV to be something you usually refer to in daily life. For example, nobody says his department's name is 'EL ENG', it should be EE! I think common sense would work here, and in the future, I'll try to create a mapping from Dep's Abbv -> Ninja's Abbv to save some headache. 

* Finally, you will also need the course number. ECON 100A's course number will be simply 100A. Please don't forget letter like 'C' for Cross-listed or 'AC' for American Culture. In other words, it's the class you want to download the exams for. This will be called **[COURSE NUMBER]**.

Good, you are done! Time to open the terminal and get your exams! Navigate to the folder where you saved ninja_scraper.py or ninja_scraper_py3k.py in.

The syntax will be
```
python scrape_ninja.py [DEPARTMENT ABBV] [NINJA ABBV] [COURSE NUMBER]
or
python3 scrape_ninja_py3k.py [DEPARTMENT ABBV] [NINJA ABBV] [COURSE NUMBER]
```

For example, if I want to get MATH 54's exams, I would type
```
python scrape_ninja.py MATH MATH 54
or
python3 scrape_ninja_py3k.py MATH MATH 54
```

The result (for the above example):
![Result1](https://raw.github.com/kqdtran/ninjascraper/master/img/result1.png)

![Result2](https://raw.github.com/kqdtran/ninjascraper/master/img/result2.png)

Simple? Don't let the long description scared you. GO GET YOUR EXAMS AND ACE THE FINALS!

## FAQs
**Q**: Why don't you write something automatically get exams for us without too many additional arguments like what Vaishaal did for CS?

**A**: I would love to, but I need to study for my finals next week too... Beside, I don't really know how to do it at the moment. I will try to look into that when I can!

**Q**: How do I download the .py file(s)? I saved it from Github but it turned out to be some sort of DOCTYPE HTML file?

**A**: You need to download the RAW file. Click on the .py file and then the RAW tab on the top right to view/download it. You should be able to get something like this https://raw.github.com/kqdtran/ninjascraper/master/scrape_ninja.py.

**Q**: Can I run this with Python[Insert Python Version here]?

**A**: Yup! Python3 and Python2 (2.6+) are supported. (Or at least I tested with both 2k and 3k on my local machine and they all worked fine...)

**Q**: Do I have to install BeautifulSoup4 for this to work?

**A**: I believe so! It's fairly straightforward and only takes a couple of minutes, so please go ahead and do it to save you some headache later on.  

**Q**: It's not working! 

**A**: Have you checked if you followed all the steps above (download BS4, Python2.6+, accurate abbreviations for both departments and ninja, etc.)? If it still doesn't work after that, send me an email (please specify what commands you tried) and I'll try to retest it and download the exams for you. No worries!

**Q**: Why is v1.2 taking soooooo long to run?

**A**: It should be, unfortunately. We're scraping through every combination of professor's last name, semester, year, etc. Please be patient!

**Q**: This is so cool! Thanks!

**A**: You're welcome :) Please say thanks to Vaishaal Shankar as well. 

## Contact Me
Please let me know if there is any bug, or if it's not working for you (see the last Q&A above). My email is a combination of those strings: "berkeley.edu", "@", "khoatran".

## Original Description by Vaishaal Shankar
https://github.com/Vaishaal/ninjascraper

gets exams from ninjacourses

Super duper beta!

only works for cs courses atm :P, and only works for finals.
defaults to cs70. Downloads pdf files to local directory.
Usage: (This will download all 61c final exams from ninjacourses)
```
python scrape_ninja.py 61C 
```
