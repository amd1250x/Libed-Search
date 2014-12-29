import yaml
from lxml import html
import requests
from getListOfSubjects import getSubjectsFromReq



arts = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CAH%2CArts%2FHumanities+%28was+Other+Humanities%29%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
bios = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CBIOL%2CBiological+Sciences%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
hist = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CHIS%2CHistorical+Perspectives%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
lit = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CLITR%2CLiterature%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
math = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CMATH%2CMathematical+Thinking%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
phys = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CPHYS%2CPhysical+Sciences%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'
socs = 'https://onestop2.umn.edu/courseinfo/viewSearchResults.do?campus=UMNTC&swapNow=N&search=Search&searchTerm=UMNTC%2C1153%2CSpring%2C2015&searchSubjects=****|****&searchCatalogNumber=&searchClassroom=true&searchPrimarilyOnline=true&searchOnline=true&searchOpenSections=true&searchLowerStartTime=00%3A00%2C12%3A00&searchUpperEndTime=23%3A59%2C11%3A59&searchMon=true&searchTue=true&searchWed=true&searchThu=true&searchFri=true&searchSat=true&searchSun=true&searchLowerLevelLimit=0%2C0xxx&searchUpperLevelLimit=9999%2C9xxx&searchLowerCreditLimit=0&searchUpperCreditLimit=9999&searchCourseAttributes=CLE%2CSOCS%2CSocial+Sciences%2Ctrue&searchInstructorName=&searchCourseTitle=&searchSessionCodes=ALL%2CALL&searchLocations=TCEASTBANK%2CEast+Bank&searchLocations=TCWESTBANK%2CWest+Bank&searchLocations=STPAUL%2CSt.+Paul&searchLocations=ROCHESTER%2CRochester&searchLocations=OFFCAMPUS%2COff+Campus+TC&campus=UMNTC'

subjectLinks = [arts, bios, hist, lit, math, phys, socs]

class subject():
    def __init__(self, name, link, relsubs):
        self.name = name
        self.link = link
        self.relsubs = []

    

    

for i in range(len(subjectLinks)):
    subjectLi






