#test api respond
import json
import requests

r = requests.get('https://covid19.th-stat.com/api/open/today')
r.json()
data = json.loads(r.text)
data = json.dumps(data)
#data2 = r.json()
#from pprint import pprint
#pprint(r.json())
#print(r.text)
#data2 = {"death":"243", "alive":"222"}
#data2.json()
#data2 = {"line":{"type": "text","text":[{"ติดเชื้อสะสม : ", (c.json())['Confirmed']},{"หายแล้ว : ", (c.json())['Recovered']},{("รักษาอยู่ใน รพ. : ", (c.json())['Hospitalized']},{"เสียชีวิต : ", (c.json())['Deaths']}]}}
#json_str = json.dump(data)
answer_function = '{"line":{"text": ' + data + ',"type": "text"} }'
#print(data)

#print (answer_function)


print("ติดเชื้อสะสม : ", (r.json())['Confirmed'])
print("หายแล้ว : ", (r.json())['Recovered'])
print("รักษาอยู่ใน รพ. : ", (r.json())['Hospitalized'])
print("เสียชีวิต : ", (r.json())['Deaths'])



"""
covid = {
    "type": "text",
    "text":
    [
        {"ติดเชื้อสะสม : ", (r.json())['Confirmed']},
        {"หายแล้ว : ", (r.json())['Recovered']},
        {("รักษาอยู่ใน รพ. : ", (r.json())['Hospitalized']},
        {"เสียชีวิต : ", (r.json())['Deaths']}
    ]
}
"""

"""
    r.json() = {
    "line":{    
    "type": "text",
    "text":
    [
        {"ติดเชื้อสะสม : ", (r.json())['Confirmed']},
        {"หายแล้ว : ", (r.json())['Recovered']},
        {("รักษาอยู่ใน รพ. : ", (r.json())['Hospitalized']},
        {"เสียชีวิต : ", (r.json())['Deaths']}
    ]
    }
    }
"""