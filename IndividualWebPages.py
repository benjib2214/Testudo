# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 21:22:39 2018

@author: Alexander Davydov
"""

from WebScanner import getData
from bs4 import BeautifulSoup
import time
from joblib import Parallel, delayed
from dataframe import AllCourse

def extractHTMLData(htmls,classes):
    if htmls == None: 
        return None
    returnInfo = []
    for col in range(len(htmls)):
        soup = BeautifulSoup(htmls[col], "html.parser")
        
        
        courses = []
        courseName = soup.find_all('span', class_ = "course-title")[0].get_text()
        for course in soup.find_all('div', class_ = "course-id"):
            courses.append(course.get_text())
        j = 0
        maxim = 0
        for i in range(len(soup.find_all('span', class_ = "section-id"))):
            professors = soup.find_all('span', class_ = "section-instructor")[i].get_text()
            #print(professors)
            sections = soup.find_all('span', class_ = "section-id")[i].get_text().strip()
            #print(sections)
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
            #print (course)
            openseats = soup.find_all('span', class_ = "open-seats-count")[i].get_text()
            totalseats = soup.find_all('span', class_ = "total-seats-count")[i].get_text()
            returnInfo.append((course,sections,None,professors,openseats,totalseats,None))
            #print (totalseats, openseats)
            #building = soup.find_all('span', class_ = "building-code")[i].get_text()
            #classroom = soup.find_all('span', class_ = "class-room")[i].get_text()
            #location = building + " " + classroom
            #print (location)
            #print ("\n")
    return returnInfo
start = time.time()
htmls = getData()
end = time.time()
print (end - start)


classes = AllCourse()
information = Parallel(n_jobs=20)(delayed(extractHTMLData)(htmls[row],classes) for row in range(len(htmls)))
for i in range(len(information)):
    if information[i] == None:
        continue
    for j in range(len(information[i])):
        classes.addSectionInfo(information[i][j][0],information[i][j][1],information[i][j][2],information[i][j][3],information[i][j][4],information[i][j][5],information[i][j][6])
classes.printAllCourseInformation()
print ("Finished")
end2 = time.time()
print (end2 - end)
#print (classes)


