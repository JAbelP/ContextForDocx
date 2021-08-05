import os
import docx
from easygui import *
import sys


class slectItem:
    def __init__(self,dir,contextKey):
        self.dir = dir
        self.contextKey = contextKey

    def get_context(self):
        return self.contextKey

    def get_dir(self):
        return self.dir
    

whereToCheck=""
refrenceArray = []
refrenceArrayButString = []

pythonFileLocation = os.getcwd()
#check if the textFile exists in directory
if os.path.isfile(os.path.join(pythonFileLocation,"config.txt")):
    print(os.path.join(pythonFileLocation,"config.txt"))
    print("File found loading")
    configText = open("config.txt","r+")
    directorySelect = configText.readline()
    print(directorySelect)
    whereToCheck = directorySelect
    print("Where to check: " + whereToCheck)
else:
    print("file not found creating config.txt")
    #creating text file
    #select directory
    directoryToLookIn = diropenbox()
    
    with open("config.txt",'w') as fp:
        fp.write(directoryToLookIn)
        fp.close()
    whereToCheck = directoryToLookIn
    print("Where to check: " + whereToCheck)

while 1:
    try:
        searchTerm = enterbox("What are you looking for?: ","Search Menu")
        if searchTerm:
            pass
        else:
            sys.exit(0)


        searchTerm = searchTerm.casefold()
        for wordDoc in os.listdir(whereToCheck):
            print(wordDoc) 
        for wordDoc in os.listdir(whereToCheck):
            fileName = os.fsdecode(wordDoc)

            if fileName.endswith(".docx") == True and fileName.startswith("~$") == False:
                analizeDoc = docx.Document(os.path.join(whereToCheck,fileName))
                pathForFile = os.path.join(whereToCheck,fileName)
        
                
                readingPara = analizeDoc.paragraphs
                for para in readingPara:
                    compareA = para.text.casefold()
                    if searchTerm in compareA:
                        #addToRefrenceArray = slectItem(analizeDoc,compareA)
                        addToRefrenceArray = slectItem(pathForFile,compareA)
                        refrenceArray.append(addToRefrenceArray)
        for refrencess in refrenceArray:
            refrenceArrayButString.append(refrencess.get_context())

        msg = "Please select the best refrence"
        title = "select"
        if(len(refrenceArrayButString)>0):
            choices = refrenceArrayButString
        if(len(refrenceArrayButString)==0):
            choices = ["Nothing was found, please click cancel to avoid a bug :)"]#come up with a better solution dummy.
        selection  = multchoicebox(msg,title,choices)
        if selection:
            pass
        else:
            sys.exit(0)
        for para in refrenceArray:
            
            if para.get_context() in selection:
                os.system("start " + para.get_dir())
                
        msg = "Search again? "
        title = "Again?"
        if ccbox(msg,title):
            refrenceArray.clear()
            refrenceArrayButString.clear()
            pass
        else:
            sys.exit(0)
    except :
        if exceptionbox():
            pass
        else:
            sys.exit(0)
    

        
