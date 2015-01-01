import yaml

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

    def __str__(self):
        return self.course_id + "\n" + \
               self.subject + "\n" + \
               self.catalog_number + "\n" + \
               self.title + "\n" + \
               self.diversified_core + "\n" + \
               self.designated_theme + "\n" + \
               str(self.writing_intensive)

def getSubjectCatalogList():
    lst = []
    for i in range(len(coursesList)):
        lst.append([coursesList[i].subject, \
                    coursesList[i].catalog_number])
    return lst    

def countLibEds():
    c = 0
    for i in range(len(coursesList)):
        if coursesList[i].diversified_core != "":
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

def getDiversifiedCores():
    lst = []
    for i in range(len(coursesList)):
        if coursesList[i].diversified_core not in lst and \
           coursesList[i].diversified_core != None:
            lst.append(coursesList[i].diversified_core)
    return lst


def countAllInDivCore(core):
    n = 0
    for i in range(len(coursesList)):
        if coursesList[i].diversified_core == core:
            n += 1
    return n

def getSubjectCatalogList(core):
    lst = []
    for i in range(len(coursesList)):
        if coursesList[i].diversified_core == core:
            lst.append([coursesList[i].subject, \
                        coursesList[i].catalog_number])
    return lst
            
def getCourseIndexFromSubjectAndNum(tup):
    sub = tup[0]
    num = tup[1]
    for i in range(len(coursesList)):
        if coursesList[i].subject == sub and \
           coursesList[i].catalog_number == num:
            return i
            
def getListOfCoursesFromCore(core):
    lst = []
    for i in range(len(coursesList)):
        if coursesList[i].diversified_core == core:
            lst.append([coursesList[i].subject, \
                        coursesList[i].catalog_number])
    return lst
