import pandas as pd

data = ['Amy', 13, 'girl']

s = pd.Series(data, index = ['Name', 'Age', 'Sex'])

dataDic = {
    'Name' : 'Amy',
    'Age' : 13,
    'Sex' : 'girl'
}

sd = pd.Series(dataDic)

print(s)
print(sd)
