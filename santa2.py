import pandas as pd
import random
import ezgmail
from tkinter.filedialog import askopenfilename

def send_email(x):
    if x.language == 'Spanish':
        subject = f"{x.personName}'s Regalo Secreto"
        body = f"""Hola {x.personName},
Se te ha asignado una persona muy especial para darle un regalo esta Navidad. Esa persona es {x.giftRecipientPerson}.
¿Quién te va a dar un regalo a ti? Shh, eso es un secreto ...
            
¡Feliz Navidad!"""

    else:
        subject = f"{x.personName}'s Secret Santa Assignment"
        body = f"""Hello {x.personName},
                
You have been assigned a very special person to give a gift to this Christmas. The person you have assigned is {x.giftRecipientPerson}.
Who is giving you a gift? Shh, that's a secret.... 
            
Merry Christmas!"""

    ezgmail.send(x.contact,subject,body)
    return

filenameforReading = askopenfilename()
people_df = pd.read_csv(filenameforReading)

while True:
    people_df['giftRecipientID'] = -1
    #print(people_df)
    try:
        for id in list(people_df.index):
            #print(id)
            #print(people_df.loc[id, 'personName'])
            notFamilyBool = people_df.loc[id, 'familyUnit'] != people_df['familyUnit']
            #print(notFamilyBool)
            notFamily = people_df[notFamilyBool].index
            #print(notFamily)
            alreadyAssignedID = people_df['giftRecipientID']
            #print(alreadyAssignedID)
            #print(set(notFamily)-set(alreadyAssignedID))
            people_df.loc[id, 'giftRecipientID'] = random.choice(list(set(notFamily)-set(alreadyAssignedID)))
        break
    except:
        continue

people_df['giftRecipientPerson'] = people_df['giftRecipientID'].apply(lambda x: people_df.loc[x, 'personName'])
people_df.apply(send_email,axis=1)
people_df.to_csv(f"{filenameforReading[:-4]}_results.csv", index = False)