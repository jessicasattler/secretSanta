import pandas as pd
import random
import ezgmail
from tkinter.filedialog import askopenfilename
filenameforReading = askopenfilename()
#filenameforReading = 'peopleSattler.csv'
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

def send_email(x):
    subject = f"{x.personName}'s Secret Santa Assignment"
    body = f"""Hello {x.personName},
                
You have been assigned a very special person to give a gift to this Christmas. The person you have assigned is {x.giftRecipientPerson}.

Who is giving you a gift? Shh, that's a secret.... 
            
Merry Christmas!"""
    ezgmail.send(x.contact,subject,body)

people_df.apply(send_email,axis=1)
people_df.to_csv(f"{filenameforReading[:-4]}_results.csv", index = False)
#while len(giftRecipienPool) !== 0:





