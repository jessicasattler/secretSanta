import pandas as pd
import random
from tkinter.filedialog import askopenfilename
#filenameforReading = askopenfilename()
filenameforReading = 'peopleSattler.csv'
people_df = pd.read_csv(filenameforReading)
people_df['giftRecipientID'] = -1
#print(people_df)
for id in list(people_df.index):
    #print(id)
    print(people_df.loc[id, 'name'])
    notFamilyBool = people_df.loc[id, 'familyUnit'] != people_df['familyUnit']
    #print(notFamilyBool)
    notFamily = people_df[notFamilyBool].index
    print(notFamily)
    alreadyAssignedID = people_df['giftRecipientID']
    print(alreadyAssignedID)
    print(set(notFamily)-set(alreadyAssignedID))
    people_df.loc[id, 'giftRecipientID'] = random.choice(list(set(notFamily)-set(alreadyAssignedID)))

print(people_df)
#while len(giftRecipienPool) !== 0:





