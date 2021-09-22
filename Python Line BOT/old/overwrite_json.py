#test api respond
import json
import requests
from types import SimpleNamespace


r = requests.get('https://covid19.th-stat.com/api/open/today')
r.json()
data = r.json()
#x = json.dumps(data)
#y = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
#print(y.confirmed)
#Confirm = [Confirmed['Confirmed']] for Confirm in data['']

#prices = [item['Price'] for item in data['results']]

from pprint import pprint
#pprint(r.json())
#print(data)

"""
print("ติดเชื้อสะสม : ", (data())['Confirmed'])
print("หายแล้ว : ", (data())['Recovered'])
print("รักษาอยู่ใน รพ. : ", (data())['Hospitalized'])
print("เสียชีวิต : ", (data())['Deaths'])
"""
#print(f"Hello\nWorld!")