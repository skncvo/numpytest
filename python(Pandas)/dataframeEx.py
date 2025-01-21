import pandas as pd

data = [['AMY', 13, 'girl'], 
            ['BEN', 13, 'boy'],
            ['EVA', 14,  'girl'], 
            ['KIM', 14,  'girl'], 
            ['NEO', 14, 'boy']]

dataDic = {'Name' :  ['Amy', 'Ben', 'Eva', 'Kim', 'Neo'],
            'Age' : [13, 13, 14, 14, 14],
            'Sex' : ['girl', 'boy', 'girl', 'girl', 'boy']          
           }

df = pd.DataFrame(data, columns=['Name', 
                                 'Age',
                                 'Sex'])

dfd = pd.DataFrame(dataDic)

#data Save
dfd.to_csv('dataDictionary.csv')
dfd.to_excel('dataDictionary.xlsx')

print(df)
print(dfd)