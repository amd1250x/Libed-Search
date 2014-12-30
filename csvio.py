import yaml
from lxml import html
import requests
from getListOfSubjects import *
import csv

class libedreq():
    def __init__(self, name, link, relsubs = []):
        self.name = name
        self.link = link
        self.relsubs = relsubs


def readfile(coursei):
    reader = csv.reader(open('courseTitles.csv', 'rb'), \
                        delimiter=',', quotechar='|')
    csvcol = []
    for col in reader:
        if col[coursei] != "":
            csvcol.append(col[coursei])
    
    return csvcol


def writefile():
    ARTS = libedreq("Arts", subjectLinks[0], getSubjectsFromReq(subjectLinks[0]))
    BIOS = libedreq("Bios", subjectLinks[1], getSubjectsFromReq(subjectLinks[1]))
    HIST = libedreq("Hist", subjectLinks[2], getSubjectsFromReq(subjectLinks[2]))
    LIT  = libedreq("Lit",  subjectLinks[3], getSubjectsFromReq(subjectLinks[3]))
    MATH = libedreq("Math", subjectLinks[4], getSubjectsFromReq(subjectLinks[4]))
    PHYS = libedreq("Phys", subjectLinks[5], getSubjectsFromReq(subjectLinks[5]))
    SOCS = libedreq("Socs", subjectLinks[6], getSubjectsFromReq(subjectLinks[6]))

    libedreqlist = [ARTS, BIOS, HIST, LIT, MATH, PHYS, SOCS]


    writer = csv.writer(open('courseTitles.csv', 'w+'), \
                        delimiter=',', quotechar='|', \
                        quoting=csv.QUOTE_MINIMAL)

    
    for i in range(max(len(libedreqlist[0].relsubs), \
                       len(libedreqlist[1].relsubs), \
                       len(libedreqlist[2].relsubs), \
                       len(libedreqlist[3].relsubs), \
                       len(libedreqlist[4].relsubs), \
                       len(libedreqlist[5].relsubs), \
                       len(libedreqlist[6].relsubs))):
        rowelements = []
        for j in range(len(libedreqlist)):
            try:
                rowelements.append(libedreqlist[j].relsubs[i])
            except:
                rowelements.append("")
        writer.writerow(rowelements)

    print libedreqlist[6].relsubs
    
    

def tryToGetSubjects(i):
    try:
        return readfile(i)
    except:
        writefile()
        readfile(i)
