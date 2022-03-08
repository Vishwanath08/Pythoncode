import csv
#converting csv to list of lists
path = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Student_marks_list.csv"
file = open(path,newline = '')
reader = csv.reader(file)
data = [row for row in reader]
name=[]
mat=[]
bio=[]
eng=[]
phy=[]
chem=[]
hin=[]
subs = []
#subject name stored in subs
for i in range(1,7):
    subs.append(data[0][i])
print(subs)
for i in range(1,len(data)):
#name of students stored separately
    name.append(data[i][0])
#marks of students are stored separately as integers
    mat.append(int(data[i][1]))
    bio.append(int(data[i][2]))
    eng.append(int(data[i][3]))
    phy.append(int(data[i][4]))
    chem.append(int(data[i][5]))
    hin.append(int(data[i][6]))
#totals marks of each students is stored 
marks=[]
for i in range(0,len(data)-1):
    s=0
    s=mat[i]+bio[i]+eng[i]+phy[i]+chem[i]+hin[i]
    marks.append(s)
#marks is copied to mark
mark=marks[:]
print(mark,marks)
#mark is sorted and reversed
mark.sort(reverse=True)
print(mark)
#index of the top three marks is found and name is stored in first,second,third using the index
ma1=marks.index(mark[0])
first=name[ma1]
ma1=marks.index(mark[1])
second=name[ma1]
ma1=marks.index(mark[2])
third=name[ma1]
#maximum mark is found and index is stored in lst
lst=[]
mm1=max(mat)
lst1=[]
for i in range(0,len(mat)):
    if(mat[i]==mm1):
        lst1.append(i)
lst.append(lst1)

mm1=max(bio)
lst1=[]
for i in range(0,len(bio)):
    if(bio[i]==mm1):
        lst1.append(i)
lst.append(lst1)

mm1=max(eng)
lst1=[]
for i in range(0,len(eng)):
    if(eng[i]==mm1):
        lst1.append(i)
lst.append(lst1)

mm1=max(phy)
lst1=[]
for i in range(0,len(phy)):
    if(phy[i]==mm1):
        lst1.append(i)
lst.append(lst1)

mm1=max(chem)
lst1=[]
for i in range(0,len(chem)):
    if(chem[i]==mm1):
        lst1.append(i)
lst.append(lst1)

mm1=max(hin)
lst1=[]
for i in range(0,len(hin)):
    if(hin[i]==mm1):
        lst1.append(i)
lst.append(lst1)

#using the index the lst students scored the highest marks from each subject is printed
for i in range(0,len(subs)):
    print("Topper in "+subs[i]+" is ",end=" ")
    a=lst[i]
    for i in range(0,len(a)):
        if(i==len(a)-1):
            print(name[a[i]],end=" ")
        else:
            print(name[a[i]],end=",")
    print()

print("Best students in the class are "+first+","+second+","+third)



        
