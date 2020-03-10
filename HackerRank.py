#Say Hello World
print("Hello, World!")

#Arithmetic Operators
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)

#Division
c=int(input())
d=int(input())
print(c//d)
print(c/d)

#Loops
N=int(input())
if(1<=N<=20):
    for N in range(N):
        print(N**2)

#Write a function
def is_leap(year):
    if(year %4==0):
      if(year %100==0):
          if(year%400==0):
            return True
          return False
      return True
    else:
      return False



year = int(input())
print(is_leap(year))
