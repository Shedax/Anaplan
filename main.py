import pandas as pd
import requests

def task1():
    data1 = pd.read_excel('./test_data.xlsx', sheet_name='Score')
    data2 = pd.read_excel('./test_data.xlsx', sheet_name='Attemps')
    data3 = data2.groupby('Player', as_index=False).max()
    data4 = data1.merge(data3, how='outer')
    data4.insert(3, 'User', 'bogdan.shevlyakov@teamvalue.ru', True)
    data4.to_excel('task.xlsx', index=False)

def task2():
    headers = {'Authorization': 'Basic',
               'encoded_username': 'password'}
    requests.post('https://auth.anaplan.com/token/authenticate',
                  auth=('bogdan.shevlyakov@teamvalue.ru', 'Bkmbxf42201'), headers=headers)

task1()
task2()