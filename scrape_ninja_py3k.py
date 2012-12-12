import sys
import os
import re
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# Use for general scraping
sem_list = ["Fall", "Spring", "Summer"]
year_list = [str(year) for year in range(2000, 2013)]
ways = ["", "(solution)", "solution"]
tests = ['Midterm', 'Midterm 1', 'Midterm 2', 'Midterm 3', 'Final']

# Use for scrape_prof specifically
two_list = ['CYPLAN', 'EALANG', 'ELENG', 'LDARCH', 'NESTUD', 'PBHLTH']
three_list = ['AGRCHM', 'BIOENG', 'CHMENG', 'CIVENG', 'COGSCI', 'COMLIT', 'DEVSTD',
                    'ENVDES', 'ENVSCI', 'ETHSTD', 'ETHGRP', 'INDENG', 'LANPRO', 'MATSCI',
                    'MEDST', 'MECENG', 'MILAFF', 'MILSCI', 'NATRES', 'NAVSCI', 'NUCENG',
                    'POLSCI', 'PUBPOL', 'SOCWEL', 'VISSCI', 'VISSTD']
four_list = ['CRITTH', 'EURAST', 'PHYSED']

def change_dep_match_url(dep="MECENG"):
    if dep == 'LS':
        new_dep = 'L%20&%20S'
    elif dep == 'SASIAN':
        new_dep = 'S%20ASIAN'
    elif dep == 'MESTU':
        new_dep = 'M%20E%20STU'
    elif dep in two_list:
        new_dep = dep[:2] + '%20' + dep[2:]
    elif dep in three_list:
        new_dep = dep[:3] + '%20' + dep[3:]
    elif dep in four_list:
        new_dep = dep[:4] + '%20' + dep[4:]
    else:
        new_dep = dep
    return new_dep

def is_semester(string):
    return "Fall " in string or "Spring " in string or "Summer " in string 

def scrape_prof(department="COMPSCI", course="70"):
    base_url = "http://ninjacourses.com/explore/1/course/"
    output_set = set()
    department = change_dep_match_url(department)
    url = base_url + department + '/' + course + '/'
    html = urlopen(url).read().decode()
    soup = BeautifulSoup(html)
    scrape_result = soup.find_all(href=re.compile("/ratings/view/instructor/"))

    # Scrape for Prof's Last Name, append result to a set
    for result in scrape_result:
        prof_name = result.text.split()[0]
        if prof_name[-1] == ',':
            prof_name = prof_name[:-1]
        if re.match("^[A-Za-z_-]+$", prof_name):
            output_set.add(prof_name)
    return output_set

def scrape_hkn(abv="CS", course="70"):
    prof_year = {} 
    html = urlopen("https://hkn.eecs.berkeley.edu/coursesurveys/course/{0}/{1}".format(abv, course))
    soup = BeautifulSoup(html) 
    tables = soup.find_all("table")[1] 
    links = tables.find_all("a") 
    current_semester = None 
    current_tuple = ()
    for i in links:
        text = str(i.text)
        if is_semester(text):
            if current_semester:
                prof_year[current_semester] = current_tuple 
                current_tuple = () 
            current_semester = text 
        else:
            current_tuple += (text,) 
    prof_year[current_semester] = current_tuple
    return prof_year

# Works only for CS courses. You only need to provide one argument
def scrape_ninja_cs(course="70", department="COMPSCI", abv="CS"):
    prof_year = scrape_hkn(abv, course)
    base_url = "http://media.ninjacourses.com/var/exams/1/{0}/{1}%20{2}%20-%20{3}%20{4}%20-%20{5}%20-%20{6}%20{7}.pdf" 
    exists = {}  
    for semester, profs in prof_year.items():
        sem, year = tuple(semester.split())
        for test in tests:
            for prof in profs:            
                for way in ways:
                    try:
                        prof = prof.split()[-1] 
                        test_split = test.split() 
                        if len(test_split) == 1: 
                            url = base_url.format(department, abv, course, sem, year, prof, test, way) 
                            if not way:
                                url = url[:-7] + ".pdf"
                        elif len(test_split) == 2: 
                            url = base_url.format(department, abv, course, sem, year, prof, test_split[0], test_split[1]) 
                            if way:
                                url = url[:-4] + "%20" + way + url[-4:]
                        urlopen(url)
                        exists[str(profs + (test, way)) + " " + semester] = url
                    
                    except Exception as e:
                        pass
                
    # Download them into your local folder
    for info, url in exists.items():
        print(url)
        urlretrieve(url, abv + course + '/' + info + ".pdf")

# Modified to temporarily work with ANY other courses
def scrape_ninja(department="ECON", abv="ECON", course="100B"):
    base_url = "http://media.ninjacourses.com/var/exams/1/{0}/{1}%20{2}%20-%20{3}%20{4}%20-%20{5}%20-%20{6}%20{7}.pdf" 
    exists = {}
    prof_list = scrape_prof(department, course)
    for prof in prof_list:
        for year in year_list:
            for sem in sem_list:
                for test in tests:
                    for way in ways:
                        try: 
                            test_split = test.split() 
                            if len(test_split) == 1: 
                                url = base_url.format(department, abv, course, sem, year, prof, test, way)
                                if not way:
                                    url = url[:-7] + ".pdf"
                            elif len(test_split) == 2: 
                                url = base_url.format(department, abv, course, sem, year, prof, test_split[0], test_split[1])
                                if way:
                                    url = url[:-4] + "%20" + way + url[-4:]
                            urlopen(url)
                            exists[str((str(prof), test, way)) + " " + sem + " " + year] = url
                    
                        except Exception as e:
                            pass

    # Download them into your local folder
    for info, url in exists.items():
        print(url)
        urlretrieve(url, abv + course + '/' + info + ".pdf")

if len(sys.argv) == 4:
    dir_name = str(sys.argv[2] + sys.argv[3])
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    scrape_ninja(sys.argv[1], sys.argv[2], sys.argv[3])

elif len(sys.argv) == 2:
    dir_name = 'CS' + str(sys.argv[1])
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    scrape_ninja_cs(sys.argv[1])

else:
    print("Not enough/Wrong arguments. Please try again.") 
