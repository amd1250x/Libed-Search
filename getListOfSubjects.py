import yaml
from lxml import html
import requests

def getSubjectsFromReq(link):
    courseTitle = html.fromstring(requests.get(link).text).xpath('//h3[@class="courseTitle"]/text()')

    c = open("courses.json")
    print 'Loading courses...'
    cjson = yaml.load(c)
    
    subjects = []
    def getSubjects():
        for i in range(len(cjson['courses'])):
            if cjson['courses'][i]['subject'] not in subjects:
                subjects.append(cjson['courses'][i]['subject'])

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
