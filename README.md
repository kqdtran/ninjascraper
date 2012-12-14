Ninja Courses has finally removed/made private all of their exams, which means unfortunately we cannot scrape the exams anymore. I hope this program was useful to some of you while it lasted, and thanks :) 
============= 

Ninja Scraper
=============
Get your exams from Ninja Course!

## Versions and Changelog
* **v1.2.1** (12/12/2012): Added more specific instructions on how to run this on Windows. Also removed some redundant code in both ".py" files.
* **v1.2** (12/8/2012): Modified to take one less command-line argumment, aka no need for professor's name anymore! It will now scrape through all exams belong to professors whose names are on the Ratings tab. Also, the exams will be saved in a directory named after the course whose exams you want to search for.
* **v1.1** (12/7/2012): Modified to work with every department, but users still need the abbreviations and professor's name. Also added support for Python3.
* **v1.0** (12/6/2012): Forked from https://github.com/Vaishaal/ninjascraper.

## Features and Acknowledgements
* Download all of the exams for the course you want into your local directory.
* Currently work for EVERY course that has its exams posted on Ninja Course. 
* Worked extremely well for CS courses thanks to Vaishaal Shankar. 
* Modified to work for every course by me, but you will need to know the department's abbreviation to search for the exams (See guide below).
* There is a very, very tiny bug in v1.2. A couple of courses have exams belong to professors that are not on NinjaCourse. For example, CS174 has 4 exams belong to Prof. Bartlett, but as you can see, he doesn't have an entry on NC http://ninjacourses.com/explore/1/course/COMPSCI/174/#ratings so the scraper couldn't find him. I have yet to find a solution to this problem, but I'll try to look into it soon.

## Installation (Linux/MacOSX)
**You must have Python 2.6+ installed on your computer**. After that, just save the scrape_ninja.py (Python2) or scrape_ninja_py3k.py (Python 3) file to your local machine. 

**You will also need to install BeautifulSoup4**. The below commands should help you set up everything if you are on a Debian/Ubuntu machine. MacOSX users can find something very similar to these (see below).

#### If Python2 is the default version of Python on your machine and you want to use Python2

* Set up easy_install (if it's not there already)
```
sudo apt-get install python-setuptools
```

* Then install BeautifulSoup4 by typing:
```
sudo easy_install beautifulsoup4
```

(You can also follow the guide below for Py3k, just replace Python3 with Python2 or Python)

Yup! You are good to go. **Mac OSX users** can find a very similar guide here: http://stackoverflow.com/questions/452283/how-can-i-install-the-beautiful-soup-module-on-the-mac.

#### If Python3 is the default version of Python on your machine, or Python2 is default BUT you want to use Python3

Note: You can also use Distribute to install BS4 with Python3, but I highly recommend sticking to the traditional way below. 

* First, go to BS4's Website: http://www.crummy.com/software/BeautifulSoup/bs4/download/ and download the tarball of the latest version.
* Unpack the package by right click on it and 'Extract Here'. If you want to do it via command line, execute the command
```
tar -zxvf beautifulsoup4-4.1.3.tar.gz	 
```
inside the directory where you saved the tarball. Replace the version's name in the tar file according to the version you downloaded.
* cd into the directory that BS4 unpacked into. Do a 'ls' to make sure setup.py is there. Then, on the terminal, type
```
sudo python3 setup.py install
```

## Installation (Windows)
* First, go to http://www.python.org/getit/ and get Python based on your system architecture (X86 or X86-64). Either 3.3.0 or 2.7.3 should work!
* Next, you need to add Python to your Windows Path if you haven't done so already. To do this, the easiest way is to go to Control Panel => System => Advanced System Settings. Click on Environment Variables. Then on the bottom, find the variable Path in System Variables. Click on edit, and add the following lines to it (for Python 2.7, similarly for other versions)
```
C:\Python27;C:\Python27\Lib;C:\Python27\Scripts
``` 
. Don't forget to separate each path with a semicolon! Try to go on Window's Command Line and type 'python'. Python should then be automatically started.

![Edit Path on Windows](https://raw.github.com/kqdtran/ninjascraper/master/img/pathedit.png)

* Nearly done! Now download the tar.gz file from http://www.crummy.com/software/BeautifulSoup/bs4/download/. Extract it, then 'cd' to where you extracted the file, and run
```
python setup.py install
```
. BeautifulSoup4 will be installed and added to the current version of Python for you. Cool!

At this point, you should have BeautifulSoup4 installed on your machine. **TIME TO GET THE EXAMS.**

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

Good, you are done! Time to open the terminal and get your exams! Navigate to the folder where you saved scrape_ninja.py or scrape_ninja_py3k.py in.

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

and similarly, on Windows,

![Result on Windows](https://raw.github.com/kqdtran/ninjascraper/master/img/result_windows.png)

Simple? Don't let the long description scared you. GO GET YOUR EXAMS!

## FAQs
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

## Contact Me
Please let me know if there is any bug, or if it's not working for you (see the second to last Q&A above). Please also contact me if you have any suggestion/idea on how to improve this program. Thanks! My email is a combination of those strings: "berkeley.edu", "@", "khoatran".

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
