#Import Library
#import statements load Python code that allow us to work with the JSON data format and the HTTP protocol.
import json
import os
import requests
from flask import Flask
from flask import request
from flask import make_response

# Flask
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def MainFunction():

    #รับ intent จาก DailogflowJay
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)

    #เรียกใช้ฟังก์ชัน generate_answer เพื่อแยกส่วนของคำถาม
    answer_from_bot = generating_answer(question_from_dailogflow_raw)
    
    #ตอบกลับไปที่ Dailogflow
    r = make_response(answer_from_bot)
    r.headers['Content-Type'] = 'application/json' #การตั้งค่าประเภทของข้อมูลที่จะตอบกลับไป

    return r

def generating_answer(question_from_dailogflow_dict):

    #Print intent ที่รับมาจาก Dailogflow
    print(json.dumps(question_from_dailogflow_dict, indent=4 ,ensure_ascii=False))

    #เก็บต่า ชื่อของ intent ที่รับมาจาก Dailogflow
    intent_group_question_str = question_from_dailogflow_dict["queryResult"]["intent"]["displayName"] 

    #ลูปตัวเลือกของฟังก์ชั่นสำหรับตอบคำถามกลับ
    if intent_group_question_str == 'covid':
        answer_str = covid_today()
    elif intent_group_question_str == 'confirmed':
        answer_str = c_confirmed()
    elif intent_group_question_str == 'recovered':
        answer_str = c_recovered()
    elif intent_group_question_str == 'hospitalized':
        answer_str = c_hospitalized()
    elif intent_group_question_str == 'deaths':
        answer_str = c_deaths()   
    elif intent_group_question_str == 'test_text':
        answer_str = test_text()
    else: answer_str = "Error"

    #สร้างการแสดงของ dict 
    answer_from_bot = {"fulfillmentText": answer_str}
    
    #แปลงจาก dict ให้เป็น JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4) 
    
    return answer_from_bot
    
def test_text():
    answer_function = 'ข้อความจาก python'
    return answer_function

def covid_today():
    c = requests.get('https://covid19.th-stat.com/api/open/today')
    c.json()
    data = json.loads(c.text)
    data = json.dumps(data)
    answer_function3 = data
    #answer_function2 = '{"line":{"text": ' + data + ',"type": "text"} }'
    return answer_function3

def c_confirmed():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data['Confirmed']
    c_confirmed = json.dumps(covid)
    answer_function = 'ยอดติดเชื้อสะสม : ' + c_confirmed + ' คน'
    return answer_function

def c_recovered():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data['Recovered']
    c_recovered = json.dumps(covid)
    answer_function = 'รักษาหายแล้ว : ' + c_recovered + ' คน'
    return answer_function

def c_hospitalized():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data['Hospitalized']
    c_hospitalized = json.dumps(covid)
    answer_function = 'รักษาอยู่ในโรงพยาบาล : ' + c_hospitalized + ' คน'
    return answer_function

def c_deaths():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data['Deaths']
    c_deaths = json.dumps(covid)
    answer_function = 'เสียชีวิต : ' + c_deaths + ' คน'
    return answer_function

#Flask 
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
