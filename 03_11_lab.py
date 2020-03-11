# -*- coding: utf-8 -*-
"""03/11 lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yc8BVBdyvkiEGfGM5QAZPKFbcO0oKVxR
"""

#ex 19
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f"You have {cheese_count} cheeses!") # Here f stands for formatting 
  print(f"You have {boxes_of_crackers} boxes of crackers!") 
  print("Man that's enough for a party!")
  print("Get a blanket.\n") #new line after string
print("We can just give the function numbers directly:") #Prints string 
cheese_and_crackers(20, 30) 
 
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#Study drills
def my_func(c):
  print("It reverses string")
  return c[::-1]

my_func("Hello")

c="Hi"
my_func(c)

my_func(c="Reversed!")

# ex 21
def add(a, b):
  print(f"ADDING {a} + {b}")
  return a + b

def subtract(a, b):
  print(f"SUBTRACTING {a} - {b}")
  return a - b

def multiply(a, b):
  print(f"MULTIPLYING {a} * {b}")
  return a * b

def divide(a, b):
  print(f"DIVIDING {a} / {b}")
  return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print("That becomes: ", what, "Can you do it by hand?")

#Study Drills
def Puzzle_Formula():
  age=35
  weight=180
  height=74
  iq=50
  return age+(height-(weight*iq/2))
Puzzle_Formula()

def Inverse():
  print("We are going to find value of age")
  initial=-4391.0
  weight=180
  height=74
  iq=50
  age=initial- (height-(weight*iq/2))
  return int(age)
Inverse()

#ex 35
from sys import exit

def gold_room():
  print("This room is full of gold. How much do you take?")
  choice = input("> ")
  if "0" in choice or "1" in choice:
    how_much = int(choice)
  else:
    dead("Man, learn to type a number.")
  
  if how_much < 50:
    print("Nice, you're not greedy, you win!")
    exit(0)
  else:
    dead("You greedy!")

def bear_room():
  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")
  print("How are you going to move the bear?")
  bear_moved = False

  while True:
    choice = input("> ")
    if choice == "take honey":
      dead("The bear looks at you then slaps your face off.")
    elif choice == "taunt bear" and not bear_moved:
      print("The bear has moved from the door.")
      print("You can go through it now.")
      bear_moved = True
    elif choice == "taunt bear" and bear_moved:
      dead("The bear gets pissed off and chews your leg off.")
    elif choice == "open door" and bear_moved:
      gold_room()
    else:
      print("I got no idea what that means.")

def cthulhu_room():
  print("Here you see the great evil Cthulhu.")
  print("He, it, whatever stares at you and you go insane.")
  print("Do you flee for your life or eat your head?")

  choice = input("> ")
  if "flee" in choice:
    start()
  elif "head" in choice:
    dead("Well that was tasty!")
  else:
    cthulhu_room()

def dead(why):
  print(why, "Good job!")
  exit(0)

def start():
  print("You are in a dark room.")
  print("There is a door to your right and left.")
  print("Which one do you take?")
  choice = input("> ")

  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulhu_room()
  else:
    dead("You stumble around the room until you starve.")

start()