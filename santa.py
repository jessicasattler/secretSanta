import pandas as pd
import random
from tkinter.filedialog import askopenfilename
#filenameforReading = askopenfilename()
filenameforReading = 'peopleSattler.csv'
people_df = pd.read_csv(filenameforReading)
while True:
    people_df['giftRecipientID'] = -1
    #print(people_df)
    try:
        for id in list(people_df.index):
            #print(id)
            #print(people_df.loc[id, 'name'])
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

people_df['giftRecipientPerson'] = people_df['giftRecipientID'].apply(lambda x: people_df.loc[x, 'name'])
print(people_df)
#while len(giftRecipienPool) !== 0:





