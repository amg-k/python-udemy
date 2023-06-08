#ACCES CONTROL

users = ["Adam", "John", "Agnes", "Laura"]

name = input("Type a name: ")
name = name.capitalize()
'''
if (name in users):
    print("You have acces to database")
else:
    print("Acces denied")
'''
if name == "Adam" or name == "Laura":
    print("You have acces to database")
else:
    print("Acces denied")
