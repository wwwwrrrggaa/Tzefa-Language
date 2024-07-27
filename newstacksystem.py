from createdpython import *
globaldict={"INT": {}, "STR": {}, "LIST": {},"BOOLEAN":{}}
class VARSYSTEM:
    def __init__(self):
        self.dict={"INT": {}, "STR": {}, "LIST": {},"BOOLEAN":{}}
    def addvar(self,type,name,value):
        global globaldict
        newdict=globaldict
        if(name not in self.dict[type]):
            if (type == "LIST"):
                self.dict[type][name] = (LIST(name, value, True, True, type),functioncount)
            else:
                self.dict[type][name] = (VALUE(name, value, True, True, type),functioncount)
            newdict[type][name] = self.dict[type][name]

        elif(self.dict[type][name][1]!=0):
            if (type == "LIST"):
                self.dict[type][name] = (LIST(name, value, True, True, type),functioncount)
            else:
                self.dict[type][name] = (VALUE(name, value, True, True, type),functioncount)
            newdict[type][name] = self.dict[type][name]

        else:
            errore.varexistserror(name)

    def getvar(self,type,name):
        if(name not in self.dict[type]):
            errore.nameerror(type,name)
        else:
            if(self.dict[type][name][1]!=functioncount and self.dict[type][name][1]!=0):
                errore.nameerror(type,name)
            else:
                return self.dict[type][name][0]
    def updatesystem(self,newdict):
        for i in newdict:
            for j in newdict[i]:
                self.dict=newdict[i][j]
    def deletevars(self,olddict):
        for i in olddict:
            for j in olddict[i]:
                del self.dict[i][j]
    def printvars(self):
        for i in self.dict:
            print(i)
            for j in self.dict[i]:
                print(self.dict[i][j][0].value,self.dict[i][j][1])
    def tooldcall(self,olddict,olderdict):
        for i in olddict:
            for j in olddict[i]:
                del self.dict[i][j]
        for i in olderdict:
            for j in olddict[i]:
                self.dict[i][j]=olderdict[i][j]

class NODE:
    def __init__(self,value):
        self.value=value
        self.next=None
    def setnext(self,nextvalue):
        self.next=NODE(value=nextvalue)
    def setnextnode(self,next):
        self.next=next
    def getnext(self):
        return self.next
    def getvalue(self):
        return self.value
class STACK:
    def __init__(self):
        self.top=NODE(None)
        self.top.setnext(None)
    def __init__(self,value):
        self.top=NODE(value)
        self.top.setnext(None)
    def push(self,value):
        NEWONE=NODE(value)
        NEWONE.setnextnode(self.top)
        self.top=NEWONE
    def pop(self):
        value=self.top.value
        self.top=self.top.getnext()
        return value
    def changetop(self,value):
        self.top.value=value
    def readtop(self):
        return self.top.value
def Wtesti(varsystem:VARSYSTEM):
    newdict=globaldict.copy()
    newdict2=globaldict.copy()
    stack=STACK(globaldict)
    global functioncount
    functioncount=0
    varsystem.addvar("INT","JUMBOI",5)
    functioncount=1
    stack.push(newdict)
    varsystem.getvar("INT","JUMBOI")
    varsystem.addvar("INT","JUMBO",4)
    varsystem.addvar("INT","JUMB",3)
    functioncount=2
    stack.push(newdict2)
    varsystem.addvar("INT","JUMB",2)
    popped=stack.pop()


    varsystem.printvars()
#varsystem=VARSYSTEM()
#test(varsystem)
Wtesti(VARSYSTEM())