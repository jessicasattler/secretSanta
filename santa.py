import random
import ezgmail
from tkinter.filedialog import askopenfilename

filenameforReading = askopenfilename()
fileVariable = open(filenameforReading, 'r')
for idx, line in enumerate(fileVariable.readlines()):
    if idx != 0:
        people = line.split(',')
        print(people)
fileVariable.close()
class Person:

    count = 0

    def __init__(self, name, contact, family, language):
        self.id = Person.count
        self.name = name
        self.contact = contact
        self.language = language
        self.family = family 
        self.recipient = None

        Person.count += 1

    def sendEmail(self):
        if self.language == 'Spanish':
            subject = f"{self.name}'s Regalo Secreto"
            body = f"""Hola {self.name},
Se te ha asignado una persona muy especial para darle un regalo esta Navidad. Esa persona es {self.recipient}.

¿Quién te va a dar un regalo a ti? Shh, eso es un secreto ...
            
¡Feliz Navidad! """
        elif self.language == 'English':
            subject = f"{self.name}'s Secret Santa Assignment"
            body = f"""Hello {self.name},
                
You have been assigned a very special person to give a gift to this Christmas. The person you have been assigned is {self.recipient}.

Who is giving you a gift? Shh, that's a secret.... 
            
Merry Christmas!"""
        ezgmail.send(self.contact,subject,body)
    



