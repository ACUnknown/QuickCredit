## QUICK CREDIT v0.2
## Python Script to add header to a batch of JAVA source code files 
##  This is tool is made by Aharnish Pithva for anyone to use and modify for their personal use for free. 
##  You can distribute the modified file for free without written consent from me but must have the credit of original author.
##  You can support this code on github.com/ACUnknown

##-----DEFAULT PARAMETERS
#Also change the format of author in the code where needed.
import time,os,datetime


authorName = "YOUR NAME HERE"
autoProDate=1 ## IF 1 , it will take File's date of modification in Header
proDate = "12 February 2021"
proNum = 1
Desc=["","","",""]

SaveFileDirectory="Final/"

##-----ADVANCED
enable_output_footer=1 ###BETA currently doesnot support codes that take input
autoReadOutput=1

#When AUTO is off and manually pasting Output, type this to stop pasting (escape sequence phrase) 
# Change this when it is stopping automatically
escSeq="xESCx" ##Not case sensitive


#!/usr/bin/env python

# Define the filename format here.
filename = "myQ"+str(proNum)+".java"


with open(filename) as f:
    content = f.readlines()


#Adding Header

#Header Format
if(autoProDate):
    proDate= (datetime.datetime.fromtimestamp(os.path.getmtime(filename=filename)).strftime('%d-%m-%Y') )

proHeader = "/* @Author: " + authorName +"\n* @Date: " + proDate + "\n* Description: " + Desc[proNum] + "\n*/\n\n\n"

FinalStr = proHeader


#Adding Actual Code
for line in content:
    FinalStr+=line

#Adding Footer
##Turn on by setting "enable_output_footer=1" at top of code.
if(enable_output_footer):
    import subprocess

    os.system("javac myQ"+ str(proNum) + ".java")


    codeOutput=""
    if(autoReadOutput==1 and FinalStr.__contains__(".nextLine()")==0):
        codeOutput= subprocess.check_output(["java","myQ"+str(proNum)])
    else:
        os.system("java myQ"+str(proNum))

        newLineOut=""
        while(newLineOut.lower()!=escSeq.lower()):
            newLineOut=input("\nPlease copy and paste the output of file number " + str(proNum) + " (type '" + escSeq + "' to complete pasting):")
            if(newLineOut.lower()!=escSeq.lower()):codeOutput+=newLineOut+"\n"
        
    print("\nRan successfully")


    print (codeOutput)
    FinalStr+="\n\n/* OUTPUT\n"
    FinalStr+=codeOutput
    FinalStr+="\n*/"

print("Final Output saved to file is:")




print(FinalStr)


##Writing to file
f = open(SaveFileDirectory+"myQ"+str(proNum)+"Final.java","w+")

f.writelines(FinalStr)

f.close()
