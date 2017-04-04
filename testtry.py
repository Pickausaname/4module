import re
def poisk(filename):
    openfile=open(filename)
    spisok=[]
    for line in openfile:
        line=line.lstrip()
        result=re.findall('^From ([\w@.]+)',line)
        if len(result)>0:
            spisok.append(result[0])
    return spisok

def unicemail(filename):
    sp=[]
    for i in poisk(filename):
        if i not in sp:
            sp.append(i)
    return sp

def month(filename):
    openfile=open(filename)
    spisok=[]
    for line in openfile:
        line=line.lstrip()
        result=re.findall('^From [\w@.]+ [\w]+ ([\w]+)',line)
        if len(result)>0:
            spisok.append(result[0])
    return spisok

def lastmonth(filename):
    data=[i for i in month(filename)[::-1]]
    email=[d for d in poisk(filename)[::-1]]
    lister=[]
    for i in unicemail(filename):
        lister.append(i)
        lister.append(data[email.index(i)])
    return lister
    
