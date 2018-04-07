import time as tm
import matplotlib.pyplot as plot
class AllCourse:
    def __init__(self):
        self.dictionary = {}
    def addCourse(self,courseCode):
        if courseCode not in self.dictionary:
            self.dictionary[courseCode] = Course(courseCode)
    def addSectionInfo(self,courseCode, sectionNumber, room, professor, seatsFree, seatsTotal, time):
        if courseCode not in self.dictionary:
            self.dictionary[courseCode] = Course(courseCode)
        self.dictionary[courseCode].addDay(sectionNumber, room, professor, seatsFree, seatsTotal, time)
    def printAllCourseInformation(self):
        for value in self.dictionary.values():
            value.printInformation()
class Course:
    def __init__(self, courseCode):
        self.courseCode = courseCode
        self.daysInfo = {}
    def addDay(self, section, room, professor, seatsFree, seatsTotal, time):
        if section in self.daysInfo:
            self.daysInfo[section].append(DailyCourseInfo(room, professor, seatsFree, seatsTotal, time))
        else:
            self.daysInfo[section] = [DailyCourseInfo(room, professor, seatsFree, seatsTotal, time)]
    def printInformation(self):
        print(self.courseCode)
        for key,value in self.daysInfo.items():
            print(key)
            for i in range(len(value)):
                print(value[i].toString())

class DailyCourseInfo():
    def __init__(self, room, professor, seatsFree, seatsTotal, time):
        self.room = room
        self.professor = professor
        self.seatsFree = seatsFree
        self.seatsTotal = seatsTotal
        self.time = time
    def toString(self):
        return [str(self.room),str(self.professor),str(self.seatsFree),str(self.seatsTotal),str(self.time)]
def main():
    courses = AllCourse()
    courses.addSectionInfo("ENEE350","0101","Kim 1200","Baru","9","20","MW 2:00-3:15")
    courses.addSectionInfo("ENEE350","0102","Kim 1200","Baru","9","20","MW 2:00-3:15")
    courses.addSectionInfo("ENEE350","0101","Kim 1100","Baru","9","20","MW 2:00-3:15")
    courses.printAllCourseInformation()
#main()
