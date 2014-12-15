import os
#-*-coding:utf-8 -*-
#-----------------------------
#   python2.7
#   author:ZedLi
#   version:0.2
#   data:2014.9.4
#   description:批量生成文件
#-------------------------------

import re
import time

snippetTemplate = """<snippet>
    <content><![CDATA[$content]]></content>
    <tabTrigger>$trigger</tabTrigger>
    <scope>source.lua</scope>
    <description>$desc</description>
</snippet>
"""

def getClass(line):
    reg = re.compile(r'(.*?)=.*?class')
    result = reg.findall(line)
    if len(result) != 0:
        print result[0].strip()

def getFunction(line):
    reg = re.compile(r'(.*?)=.*?function\((.*?)\)')
    results = reg.findall(line)
    return results
    #for result in results:
     #   print result[0]

def replaceValue(parent,result):
    #content = result[0].strip()+"("+result[1].strip()+")" #补全的内容
    className,trigger=result[0].split(".") #类名和方法名
    content = trigger.strip()+"("+result[1].strip()+")"
    fileName = className.strip() +"-"+trigger.strip()+".sublime-snippet"
    if trigger.strip() == "ctor":
        content = className+","+result[1].strip()
        trigger = className+".ctor"
    #fileName = className.strip() +"-"+trigger.strip()+".sublime-snippet"
    desc = result[0]    #描述的内容
    template = snippetTemplate.replace("$content",content)
    template = template.replace("$trigger",trigger)
    template = template.replace("$desc",desc)
    #name = "test"+".sublime-snippet"
    path = os.getcwd()+"\lua"+"\\"+parent+"\\"+className.strip()
    #print path
    #print os.path.isdir(path)
    if os.path.isdir(path):
        #os.makedirs(path)
        f= open(path+"\\"+fileName,"w")
        f.write(template)
        f.close()
    else:
        os.makedirs(path)
        f= open(path+"\\"+fileName,"w")
        f.write(template)
        f.close()



def openFile(parent,fileName):
    with open(fileName,"r") as fp:
        line = fp.read()
        results = getFunction(line.strip())
    '''
    if len(results)>0 and results[0][0].find(".")!=-1:
        className,_ = results[0][0].split(".")
        print "\""+className.strip()+"\","
    '''
    for result in results:
        if result[0].find(".")!=-1 and not result[0].startswith("--"): #类名和方法名
            replaceValue(parent,result)
            print result
    print fileName+"-----------------------success"
    

if __name__ == "__main__":
    
    #rootDir = raw_input("input the dir:")
    start = time.time()
    for rootDir in rootDirs:
       # print rootDir
        for parents,dirNames,fileNames in os.walk(rootDir):
            x = parents.split("\\")
            parent=x[len(x)-1]
            for fileName in fileNames:
                openFile(parent,parents+"\\"+fileName)
    
    #openFile("","log.lua")
    print "---------success-------------------"
   # print 'done %.2f seconds' % (time.time()-start)
