import yaml
from lxml import html
import requests
import unicodedata
from csvio import *

arts = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CAH%2CArts%2FHumanities+%28was+Other+Humanities%29%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
bios = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CBIOL%2CBiological+Sciences%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
hist = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CHIS%2CHistorical+Perspectives%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
lit = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CLITR%2CLiterature%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
math = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CMATH%2CMathematical+Thinking%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
phys = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CPHYS%2CPhysical+Sciences%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
socs = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CSOCS%2CSocial+Sciences%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'

subjectLinks = [arts, bios, hist, lit, math, phys, socs]

cjson = open("courses.json")
cyaml = yaml.load(cjson)

coursesList = []

class Course():
    def __init__(self, course_id, subject, \
                 catalog_number, title, diversified_core, \
                 designated_theme, writing_intensive):
        self.course_id = course_id
        self.subject = subject
        self.catalog_number = catalog_number
        self.title = title
        self.diversified_core = diversified_core
        self.designated_theme = designated_theme
        self.writing_intensive = writing_intensive
        self.LESubject = ""
        self.isLibEd = False

    def __str__(self):
        return self.course_id + "\n" + \
               self.subject + "\n" + \
               self.catalog_number + "\n" + \
               self.title + "\n" + \
               self.diversified_core + "\n" + \
               self.designated_theme + "\n" + \
               str(self.writing_intensive) + "\n" + \
               self.LESubject + "\n" + \
               str(self.isLibEd)

def checkLibEd(s):
    if s.subject + str(s.catalog_number) in readfile(0):
        s.LESubject = "arts"
        s.isLibEd = True
    elif s.subject + str(s.catalog_number) in readfile(1):
        s.LESubject = "biol"
        s.isLibEd = True
    elif s.subject + str(s.catalog_number) in readfile(2):
        s.LESubject = "hist"
        s.isLibEd = True
    elif s.subject + str(s.catalog_number) in readfile(3):
        s.LESubject = "lit"
        s.isLibEd = True
    elif s.subject + str(s.catalog_number) in readfile(4):
        s.LESubject = "math"
        s.isLibEd = True
    elif s.subject + str(s.catalog_number) in readfile(5):
        s.LESubject = "phys"
        s.isLibEd = True
    elif s.subject + str(s.catalog_number) in readfile(6):
        s.LESubject = "socs"
        s.isLibEd = True

def checkAllCoursesForLibEd():
    for i in range(len(coursesList)):
        checkLibEd(coursesList[i])

def getSubjectCatalogList():
    lst = []
    for i in range(len(coursesList)):
        lst.append([coursesList[i].subject, \
                    coursesList[i].catalog_number])
    return lst    

def getLibEdSubjectCatalogList(s):
    lst = []
    for i in range(len(coursesList)):
        if coursesList[i].isLibEd == True and \
           coursesList[i].LESubject == s:
            lst.append([coursesList[i].subject, \
                        coursesList[i].catalog_number])
    return lst    

def countLibEds():
    c = 0
    for i in range(len(coursesList)):
        if coursesList[i].isLibEd == True:
            c += 1
    return c

for i in range(len(cyaml['courses'])):
    coursesList.append(Course(cyaml['courses'][i]['course_id'], \
                              cyaml['courses'][i]['subject'], \
                              cyaml['courses'][i]['catalog_number'], \
                              cyaml['courses'][i]['title'], \
                              cyaml['courses'][i]['diversified_core'], \
                              cyaml['courses'][i]['designated_theme'], \
                              cyaml['courses'][i]['writing_intensive']))


def getSubjectCatalogFromLink(s, l):
    courseTitle = html.fromstring(requests.get(l).text).xpath('//h3[@class="courseTitle"]/text()')
    for i in range(len(courseTitle)):
        courseTitle[i] = courseTitle[i][:10]
        subs = yaml.load(courseTitle[i])
        subs = subs.split(' ')
        subs[0] = yaml.load(subs[0])
        subs[0] = unicodedata.normalize('NFKD', subs[0]).encode('ascii','ignore')
        subs[0] = subs[0].split(" ")
        print subs[0]
        for j in range(len(coursesList)):
            if subs[0][0] == coursesList[j].subject and \
               subs[0][1] == coursesList[j].catalog_number:
                coursesList[j].isLibEd = True
                coursesList[j].LESubject = s
    return getLibEdSubjectCatalogList(s)

def getCourseFromSubjectAndNum(tup):
    sub = tup[0]
    num = tup[1]
    for i in range(len(coursesList)):
        if coursesList[i].subject == sub and \
           coursesList[i].catalog_number == num:
            print str(i) + "\n" + str(coursesList[i])
            

