import yaml
from getListOfSubjects import *
import random
from Tkinter import *

coursesToInclude = []

class Application(Frame):
    def getRandomCourse(self):
        print coursesToInclude
        
    def addDivCoreSocs(self):
        if self.SocsVar.get() == 1 and "SOCS" not in coursesToInclude:
            coursesToInclude.append(getSubjectCatalogList("SOCS")[random.randint(0, len(getSubjectCatalogList("SOCS")))])
        elif self.SocsVar.get() == 0:
            for i in range(len(coursesToInclude)):
                try:
                    if [coursesToInclude[i][0],coursesToInclude[i][1]] in getSubjectCatalogList("SOCS"):
                        coursesToInclude.remove([coursesToInclude[i][0],coursesToInclude[i][1]])
                except:
                    return 0

    def addDivCoreAH(self):
        if self.AHVar.get() == 1 and "AH" not in coursesToInclude:
            coursesToInclude.append(getSubjectCatalogList("AH")[random.randint(0, len(getSubjectCatalogList("AH")))])
        elif self.AHVar.get() == 0:
            for i in range(len(coursesToInclude)):
                try:
                    if [coursesToInclude[i][0],coursesToInclude[i][1]] in getSubjectCatalogList("AH"):
                        coursesToInclude.remove([coursesToInclude[i][0],coursesToInclude[i][1]])
                except:
                    return 0
                
    def addDivCoreLitr(self):
        if self.LitrVar.get() == 1 and "LITR" not in coursesToInclude:
            coursesToInclude.append(getSubjectCatalogList("LITR")[random.randint(0, len(getSubjectCatalogList("LITR")))])
        elif self.LitrVar.get() == 0:
            for i in range(len(coursesToInclude)):
                try:
                    if [coursesToInclude[i][0],coursesToInclude[i][1]] in getSubjectCatalogList("LITR"):
                        coursesToInclude.remove([coursesToInclude[i][0],coursesToInclude[i][1]])
                except:
                    return 0
                
    def addDivCoreHis(self):
        if self.HisVar.get() == 1 and "HIS" not in coursesToInclude:
            coursesToInclude.append(getSubjectCatalogList("HIS")[random.randint(0, len(getSubjectCatalogList("HIS")))])
        elif self.HisVar.get() == 0:
            for i in range(len(coursesToInclude)):
                try:
                    if [coursesToInclude[i][0],coursesToInclude[i][1]] in getSubjectCatalogList("HIS"):
                        coursesToInclude.remove([coursesToInclude[i][0],coursesToInclude[i][1]])
                except:
                    return 0
                
    def addDivCoreBiol(self):
        if self.BiolVar.get() == 1 and "BIOL" not in coursesToInclude:
            coursesToInclude.append(getSubjectCatalogList("BIOL")[random.randint(0, len(getSubjectCatalogList("BIOL")))])
        elif self.BiolVar.get() == 0:
            for i in range(len(coursesToInclude)):
                try:
                    if [coursesToInclude[i][0],coursesToInclude[i][1]] in getSubjectCatalogList("BIOL"):
                        coursesToInclude.remove([coursesToInclude[i][0],coursesToInclude[i][1]])
                except:
                    return 0
                
    def addDivCorePhys(self):
        if self.PhysVar.get() == 1 and "PHYS" not in coursesToInclude:
            coursesToInclude.append(getSubjectCatalogList("PHYS")[random.randint(0, len(getSubjectCatalogList("PHYS")))])
        elif self.PhysVar.get() == 0:
            for i in range(len(coursesToInclude)):
                try:
                    if [coursesToInclude[i][0],coursesToInclude[i][1]] in getSubjectCatalogList("PHYS"):
                        coursesToInclude.remove([coursesToInclude[i][0],coursesToInclude[i][1]])
                except:
                    return 0
                
    def addDivCoreMath(self):
        if self.MathVar.get() == 1 and "MATH" not in coursesToInclude:
            coursesToInclude.append(getSubjectCatalogList("MATH")[random.randint(0, len(getSubjectCatalogList("MATH")))])
        elif self.MathVar.get() == 0:
            for i in range(len(coursesToInclude)):
                try:
                    if [coursesToInclude[i][0],coursesToInclude[i][1]] in getSubjectCatalogList("MATH"):
                        coursesToInclude.remove([coursesToInclude[i][0],coursesToInclude[i][1]])
                except:
                    return 0
                
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.getRC = Button(self)
        self.getRC["text"] = "Get a course"
        self.getRC["command"] = self.getRandomCourse
        self.getRC.pack({"side": "left"})

        self.SocsVar = IntVar()
        self.checkSocs = Checkbutton(self)
        self.checkSocs["text"] = "Socs"
        self.checkSocs["variable"] = self.SocsVar
        self.checkSocs["command"] = self.addDivCoreSocs
        self.checkSocs.pack({"side":"left"})

        self.AHVar = IntVar()
        self.checkAH = Checkbutton(self)
        self.checkAH["text"] = "AH"
        self.checkAH["variable"] = self.AHVar
        self.checkAH["command"] = self.addDivCoreAH
        self.checkAH.pack({"side":"left"})

        self.LitrVar = IntVar()
        self.checkLitr = Checkbutton(self)
        self.checkLitr["text"] = "Litr"
        self.checkLitr["variable"] = self.LitrVar
        self.checkLitr["command"] = self.addDivCoreLitr
        self.checkLitr.pack({"side":"left"})

        self.HisVar = IntVar()
        self.checkHis = Checkbutton(self)
        self.checkHis["text"] = "His"
        self.checkHis["variable"] = self.HisVar
        self.checkHis["command"] = self.addDivCoreHis
        self.checkHis.pack({"side":"left"})

        self.BiolVar = IntVar()
        self.checkBiol = Checkbutton(self)
        self.checkBiol["text"] = "Biol"
        self.checkBiol["variable"] = self.BiolVar
        self.checkBiol["command"] = self.addDivCoreBiol
        self.checkBiol.pack({"side":"left"})

        self.PhysVar = IntVar()
        self.checkPhys = Checkbutton(self)
        self.checkPhys["text"] = "Phys"
        self.checkPhys["variable"] = self.PhysVar
        self.checkPhys["command"] = self.addDivCorePhys
        self.checkPhys.pack({"side":"left"})

        self.MathVar = IntVar()
        self.checkMath = Checkbutton(self)
        self.checkMath["text"] = "Math"
        self.checkMath["variable"] = self.MathVar
        self.checkMath["command"] = self.addDivCoreMath
        self.checkMath.pack({"side":"left"})

    def cb(self):
        print "variable is", type(self.var.get())

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

        self.var = IntVar()
        c = Checkbutton(
            master, text="Enable Tab",
            variable=self.var,
            command=self.cb)
        c.pack()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
