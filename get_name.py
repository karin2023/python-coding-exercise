import os
import os.path

def get_str_btw(s,f,b):
    par = s.partition(f)
    #return(par[2].partition(b))[0][:]
    return(par[2].partition(b))[0]


path = './'
mylist = []
dirs = os.listdir(path)

for file in dirs:
    if file.endswith(".pdf"):
        str = file
        a = str
        str = get_str_btw(str,'-','-')
        b= str
        if (str != ''):
            mylist.append(str)
    elif file.endswith(".docx"):
        str = file
        str = get_str_btw(str,'-','-')
        if (str != ''):
            mylist.append(str)

print(mylist)
print()
str = "-"
print (str.join(mylist))
rename = str.join(mylist)

old = a
new = old.replace(b, rename);
print()
print(new)
