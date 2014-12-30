import yaml
from lxml import html
import requests



cjson = open("courses.json")
cyaml = yaml.load(cjson)

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

coursesList = []
for i in range(len(cyaml['courses'])):
    coursesList.append(Course(cyaml['courses'][i]['course_id'], \
                              cyaml['courses'][i]['subject'], \
                              cyaml['courses'][i]['catalog_number'], \
                              cyaml['courses'][i]['title'], \
                              cyaml['courses'][i]['diversified_core'], \
                              cyaml['courses'][i]['designated_theme'], \
                              cyaml['courses'][i]['writing_intensive']))


def test(l):

    courseTitle = html.fromstring(requests.get(l).text).xpath('//h3[@class="courseTitle"]/text()')
    subs = yaml.load(courseTitle[0])
    print yaml.load(subs.split(' ')[0]) #THIS IS IT!!
    

def getSubjectsFromReq(link):

    courseTitle = html.fromstring(requests.get(link).text).xpath('//h3[@class="courseTitle"]/text()')

    subjects = []
    def getSubjects():
        for i in range(len(coursesList)):
            if coursesList[i].subject not in subjects:
                subjects.append(coursesList[i].subject)

    getSubjects()
    def getSubjectFromPage(n):
        for i in range(len(courseTitle[n])-2):
            if courseTitle[n][i] + \
               courseTitle[n][i+1] in subjects:
                return yaml.load(courseTitle[n][i] + \
                                 courseTitle[n][i+1])
        for i in range(len(courseTitle[n])-3):
            if courseTitle[n][i] + \
               courseTitle[n][i+1] + \
               courseTitle[n][i+2] in subjects:
                return yaml.load(courseTitle[n][i] + \
                                 courseTitle[n][i+1] + \
                                 courseTitle[n][i+2])
        for i in range(len(courseTitle[n])-4):
            if courseTitle[n][i] + \
               courseTitle[n][i+1] + \
               courseTitle[n][i+2] + \
               courseTitle[n][i+3] in subjects:
                return yaml.load(courseTitle[n][i] + \
                                 courseTitle[n][i+1] + \
                                 courseTitle[n][i+2] + \
                                 courseTitle[n][i+3])

        
    def convertPageToSubject():
        for i in range(len(courseTitle)):
            courseTitle[i] = getSubjectFromPage(i)

    def removeRepeats(l):
        return list(set(l))

    convertPageToSubject()
    courseTitle = removeRepeats(courseTitle)

    return courseTitle
