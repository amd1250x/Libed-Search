import yaml
from lxml import html
import requests
from getListOfSubjects import *
import csv
from csvio import *



ARTS = libedreq("Arts", subjectLinks[0], tryToGetSubjects(0))
BIOS = libedreq("Bios", subjectLinks[1], tryToGetSubjects(1))
HIST = libedreq("Hist", subjectLinks[2], tryToGetSubjects(2))
LIT  = libedreq("Lit",  subjectLinks[3], tryToGetSubjects(3))
MATH = libedreq("Math", subjectLinks[4], tryToGetSubjects(4))
PHYS = libedreq("Phys", subjectLinks[5], tryToGetSubjects(5))
SOCS = libedreq("Socs", subjectLinks[6], tryToGetSubjects(6))

libedreqlist = [ARTS, BIOS, HIST, LIT, MATH, PHYS, SOCS]

checkAllCoursesForLibEd()

