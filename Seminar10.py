# Выполнил данное упражнение в Гугл колаб  но что то у меня там не получилось выгрузить в github
# написал код тут.
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
#Решение
data.loc[data['whoAmI']=='human','human' ]='1'
data.loc[data['whoAmI']=='robot', 'human']='0'
data.loc[data['whoAmI']=='human','robot' ]='0'
data.loc[data['whoAmI']=='robot', 'robot']='1'
data.drop('whoAmI', axis=1, inplace=True)
data