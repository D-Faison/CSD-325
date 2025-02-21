#DeJanae Faison DATE Assignment 8.2 JSON practice

import json
#file handling
from os import path

from notifypy import Notify


fileName = 'students.json'
stundentInfo = []

#Check if file exists, if not, print message
if path.isfile(fileName) is False:
    raise Exception("File Not Found")

#with file name open, append the file contents to the array
with open (fileName) as file:
    #load file
    stundentInfo = json.load(file)

#print header, \n being a line break
print("~ Original Student Information~\n")

#Function to format and display original values
def formattedValues():

    #iterate through the data in the file and display them in the desired format
    for info in stundentInfo:
        #Access the desired data from the file and convert to variable
        studentFName = info["F_Name"]
        studentLName = info["L_Name"]
        studentID = info["Student_ID"]
        studentEmail = info["Email"]

        print(f"{studentLName},{studentFName}: ID = {studentID}, Email = {studentEmail}\n")
   

listofStudents = formattedValues()

def notification():
    notification = Notify()
    notification.title = "Student List"
    notification.message = "Viewing Original Student List in Terminal "
    notification.send()
notification()





c = input("Add a new student? Y or N?\n")
while c == "Y":
   break

stundentInfo.append({
    "F_Name":"DeJanae",
    "L_Name":"Faison",
    "Student_ID":1234536576,
    "Email":"example@gmail.com"
    })

with open(fileName,'w') as json_file:
    json.dump(stundentInfo,json_file,indent=4,separators=(',',':'))
    
with open (fileName) as file:
    #load file
    stundentInfo = json.load(file)

print("~Updated List~\n")
formattedValues()

def upDATEotification():
    notification = Notify()
    notification.title = "Student List"
    notification.message = "Viewing Updated Student List in Terminal "
    notification.send()
upDATEotification()





#Resources:
#importing json file source:
#Gupta, L. (2021, July 4). Python - Append to JSON File. HowToDoInJava. https://howtodoinjava.com/python-json/append-json-to-file/
#Notifications
#Client Challenge. (2025). Pypi.org. https://pypi.org/project/notify_py/

