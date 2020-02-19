#1
for number in range (1,26):
  print(number**2)

#2
y=()
while(y!="haha"):
  y=input("Write 'It's a Loop:  ")

#3
positive=float(input())
while(positive>0):
  positive-=0.5
  print(positive)

#4
a=()
while(a!="no"):
  a=input("Do you want to continue?  ")
print("This is the end")

#Level 1 Loops

#1
for i in range(3):
  print(i)
  
  #2
list1=list(input())
i=input()
if(i in list1):
  list1.remove(i)
else:
  print(list1)

print(list1)

#4
list1=[1,2,3,4,5]
for element in list1:
  print(element**2)
  
#5
a=range(1,101)
listEven=[]
for i in range(1,101):
  if(i%2==0):
    listEven.append(i)

print(listEven)



