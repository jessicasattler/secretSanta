import pandas as pd
from tkinter.filedialog import askopenfilename
#filenameforReading = askopenfilename()
filenameforReading = 'people.csv'
people_df = pd.read_csv(filenameforReading)
print(people_df)


