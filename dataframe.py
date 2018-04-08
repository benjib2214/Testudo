import time as tm
import pickle
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
    def getSectionInfo(self,courseCode,sectionNumber,day):
        try:
            return self.dictionary[courseCode].daysInfo[sectionNumber][day].toString()
        except:
            return "invalid entry"
    def getSection(self,courseCode,sectionNumber):
        try:
            return self.dictionary[courseCode].daysInfo[sectionNumber]
        except:
            return "invalid entry"
    def generateLineGraph(self,courseCode,section):
        tmp = []
        generator = range(len(self.getSection(courseCode,section)))
        for i in generator:
            tmp.append(int(self.dictionary[courseCode].daysInfo[section][i].seatsFree))
        plot.plot(generator,tmp)
        plot.ylim(0,int(self.dictionary[courseCode].daysInfo[section][i].seatsTotal))
        plot.ylabel('Free Seats')
        plot.xlabel('Days Elapsed')
        plot.title(courseCode+' '+section)
        plot.show()
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
def pickleAllCourse(allCourse):
    binary_file = open('stored_all_classes.bin','wb')
    pickledObject = pickle.dump(allCourse.dictionary,binary_file)
    binary_file.close()
def loadAllCourse():
    binary_file = open('stored_all_classes.bin','rb')
    returns = pickle.load(binary_file)
    binary_file.close()
    return returns 
def main():
    courses = AllCourse()
    courses.addSectionInfo("ENEE350","0101","Kim 1200","Baru","20","20","MW 2:00-3:15")
    courses.addSectionInfo("ENEE350","0101","Kim 1200","Baru","16","20","MW 2:00-3:15")
    courses.addSectionInfo("ENEE350","0101","Kim 1200","Baru","13","20","MW 2:00-3:15")
    courses.addSectionInfo("ENEE350","0102","Kim 1200","Baru","9","20","MW 2:00-3:15")
    courses.addSectionInfo("ENEE350","0101","Kim 1100","Baru","9","20","MW 2:00-3:15")
    courses.printAllCourseInformation()
    pickleAllCourse(courses)
    del courses
    courses = AllCourse()
    courses.dictionary = loadAllCourse()
    courses.printAllCourseInformation()
    print(courses.getSectionInfo("ENEE350","0101",1))
    courses.generateLineGraph("ENEE350","0101")
main()
