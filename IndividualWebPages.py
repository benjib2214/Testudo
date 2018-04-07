# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 21:22:39 2018

@author: Alexander Davydov
"""

from WebScanner import getData
from bs4 import BeautifulSoup
import urllib

htmls = getData()

#url = "https://app.testudo.umd.edu/soc/search?courseId=enes100&sectionId=&termId=201808&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"

#f = urllib.request.urlopen(url)
#fp = f.read().strip()
#print (fp)
for row in range(len(htmls)):
    for col in range(len(htmls[row])):
        soup = BeautifulSoup(htmls[row][col], "html.parser")
        
        
        #print(courseNums)
        courses = []
        courseName = soup.find_all('span', class_ = "course-title")[0].get_text()
        for course in soup.find_all('div', class_ = "course-id"):
            courses.append(course.get_text())
        j = 0
        maxim = 0
        for i in range(len(soup.find_all('span', class_ = "section-id"))):
            professors = soup.find_all('span', class_ = "section-instructor")[i].get_text()
            print(professors)
            sections = soup.find_all('span', class_ = "section-id")[i].get_text().strip()
            print(sections)
            try:
                if int(sections) > maxim:
                    pass
                elif int(sections) <= maxim:
                    j += 1
                maxim = int(sections)
            except:
                pass
            
            course = courses[j]
            #days = soup.find_all('span', class_ = "section-days")[i].get_text()
            #starttime = soup.find_all('span', class_ = "class-start-time")[i].get_text()
            #endtime = soup.find_all('span', class_ = "class-end-time")[i].get_text()
            #times = days + " " + starttime + " - " + endtime
            #print (times)
            print (course)
            openseats = soup.find_all('span', class_ = "open-seats-count")[i].get_text()
            totalseats = soup.find_all('span', class_ = "total-seats-count")[i].get_text()
            print (totalseats, openseats)
            #building = soup.find_all('span', class_ = "building-code")[i].get_text()
            #classroom = soup.find_all('span', class_ = "class-room")[i].get_text()
            #location = building + " " + classroom
            #print (location)
            print ("\n")

print ("Finished")
#print (classes)


