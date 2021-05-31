import random
from art import logo
from replit import clear
print(logo)
n=0
from game_data import data
length= len(data)
item2= random.randint(0, length-1)
loop=True
while loop:
    item1=item2
    item2= random.randint(0, length-1)
    if item1==item2:
      continue
    first=data[item1]
    name= first["name"]
    profession= first["description"]
    country= first["country"]
    print(f"Compare A: {name}, a {profession}, from {country}.")
    from art import vs
    print(vs)
    second=data[item2]
    name= second["name"]
    profession= second["description"]
    country= second["country"]
    print(f"Against B: {name}, a {profession}, from {country}.")
    answer=input("Who has more followers? A or B? ").capitalize()
    if answer=="A":
      if first["follower_count"]> second["follower_count"]:
        n=n+1
        clear()
        print(logo)
        print(f"You are right. Your current score is {n}.")
      else:
        loop=False
    if answer=="B":
      if first["follower_count"]< second["follower_count"]:
        n=n+1
        clear()
        print(logo)
        print(f"You are right. Your current score is {n}.")
      else:
        loop=False
clear()
print(logo)
print(f"Sorry that's wrong. Your total score is {n}.")


