import pandas
import pandas as pd

import re

see = pd.read_csv("QCRI_demo_dataset.csv")
print(see)
# print(pd.read_csv("QCRI_demo_dataset")

row1 = see.loc[:, "Job_Description"]
print(row1)

row2 = row1.tolist()
print(row2)

emptylist = []

#replace "  " with " ", replace \n, (1), 1., a., i., and \nâ\x80¢\t

def needsCleaning(e):
    print(e)
    e = e.replace(r'\W+', " ")
    e = e.replace("\n", " ")
    e = re.sub(' +',' ', e)

    return e



# for e in row2:
#     print(e)
#     e = needsCleaning(e)
#     emptylist.append(e)
    # find_words = e.replace(r'\W+', " ")
    # replaceN = find_words.replace("\n", " ")
    # removeSpace = re.sub(' +',' ', replaceN)


see['Cleaned_Up'] = see['Job_Description'].apply(lambda e: needsCleaning(e))
print(see)

see.to_csv('cleanedQCRI2.csv')