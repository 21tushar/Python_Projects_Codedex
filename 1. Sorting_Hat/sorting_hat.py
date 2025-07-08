"""The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin
"""

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print("""Q1) Do you like Dawn or Dusk?
             1) Dawn
             2) Dusk\n""")

answer = int(input("My answer is: "))

if answer == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif answer == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input.")

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print("""\nQ2) When I’m dead, I want people to remember me as:
             1) The Good
             2) The Great
             3) The Wise
             4) The Bold\n""")

answer = int(input("My answer is: "))

if answer == 1:
  Hufflepuff += 2
elif answer == 2:
  Slytherin += 2
elif answer == 3:
  Ravenclaw += 2
elif answer == 4:
  Gryffindor += 2
else:
  print("Wrong input.")

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

print("""\nQ3) Which kind of instrument most pleases your ear?
             1) The violin
             2) The trumpet
             3) The piano
             4) The drum\n""")

answer = int(input("My answer is: "))

if answer == 1:
  Slytherin += 4
elif answer == 2:
  Hufflepuff += 4
elif answer == 3:
  Ravenclaw += 4
elif answer == 4:
  Gryffindor += 4
else:
  print("Wrong input.") 

print("\nGryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)
