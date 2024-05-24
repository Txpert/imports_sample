# def greeting(name):
#      print("Hello, " + name + "!")

# # Call the function with the argument "Alice"
# greeting("Alice")


# def add(a, b):
#      return a + b

# result = add(2, 5)
# print(result)

# add_ten = lambda a: a + 10

# print(add_ten(5))

# add_ten()

# A lambda function that adds 10 to the input

# list = []
# leeres_tupel = ()
# einfaches_tupel = (1, 2)

# erste_element = list[0]

# def call_function(func, *args):
#     return func(*args)

# def multiply(x, y):  
#     return x * y

# def add_ten(x):  
#     return x + 10

# result = call_function(multiply, 5, 6, )

# result2 = call_function(add_ten, 5)
# print(result + result2)

    
# Pass the function as an argument
# call_function(multiply)



import random

def zufallszahl_generieren():
    return random.randint(1, 100)

def benutzereingabe():
    return int(input("Gib deinen Tipp ein: "))

def vergleichen(geratene_zahl, zufallszahl):
    if geratene_zahl < zufallszahl:
        print("Zu niedrig! Versuche es erneut.\n")
        return False
    elif geratene_zahl > zufallszahl:
        print("Zu hoch! Versuche es erneut.\n")
        return False
    else:
        print("Herzlichen Glückwunsch! Du hast die Zahl erraten.")
        return True
    
def spiel():

    print("Willkommen zum Zahlenratespiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
    print("Kannst du sie erraten?\n")
   

    zufallszahl = zufallszahl_generieren()
    versuche = 0
    erraten = False

    while not erraten: 
        geratene_zahl = benutzereingabe()
        versuche += 1 #versuche = versuche + 1
        erraten = vergleichen(geratene_zahl, zufallszahl)

    print(f"richtig, du hast es in {versuche} geschafft.")

spiel()
