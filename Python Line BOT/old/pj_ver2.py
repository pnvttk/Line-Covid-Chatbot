#Import Library
#import statements load Python code that allow us to work with the JSON data format and the HTTP protocol.
import json
import os
import requests
from flask import Flask
from flask import request
from flask import make_response

#------------------------------- Google Sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
cerds = ServiceAccountCredentials.from_json_keyfile_name("cerds.json", scope)
client = gspread.authorize(cerds)
sheet = client.open("Chatbot").worksheet('Sheet1') # เป็นการเปิดไปยังหน้าชีตนั้นๆ
data = sheet.get_all_records()  # การรับรายการของระเบียนทั้งหมด


c = requests.get('https://covid19.th-stat.com/api/open/today')
c.json()
data = json.loads(c.text)
data = json.dumps(data)

# Flask
app = Flask(__name__)
@app.route('/', methods=['POST']) 

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
    if intent_group_question_str == 'บันทึกข้อมูล':
        answer_str = save_data()
    elif intent_group_question_str == 'covid':
        answer_str = covid_today()
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

def save_data(): #ฟังก์ชั่นสำหรับบันทึกข้อมูล
    ans1 = ' กรุณาบอกเวลาล่าสุดที่ได้ตรวจวัดอุณหภูมิ เช่น 09:00 หรือ "-", "จำไม่ได้"'   
    answer_function = 'จะเริ่มทำการบันทึกข้อมูล' + ans1

    return answer_function

def covid_today():
    answer_function1 = 'text from python'
    c = requests.get('https://covid19.th-stat.com/api/open/today')
    c.json()
    data = json.loads(c.text)
    data = json.dumps(data)
    #data = covid_today.json()
    #from pprint import pprint
    #pprint(r.json())
    #answer_c = 'กำลังแสดงข้อมูล' #+ r.text()
    #json_str = json.dumps(covid_today)
    #data2 = '{"line":{"type": "text","text":[{"ติดเชื้อสะสม : ", (c.json())['Confirmed']},{"หายแล้ว : ", (c.json())['Recovered']},{("รักษาอยู่ใน รพ. : ", (c.json())['Hospitalized']},{"เสียชีวิต : ", (c.json())['Deaths']}]}}'
    answer_function3 = data
    answer_function2 = '{"line":{"text": ' + data + ',"type": "text"} }'
    return answer_function3


"""
    print("ติดเชื้อสะสม : ", (covid_today.json())['Confirmed'])
    print("หายแล้ว : ", (covid_today.json())['Recovered'])
    print("รักษาอยู่ใน รพ. : ", (covid_today.json())['Hospitalized'])
    print("เสียชีวิต : ", (covid_today.json())['Deaths'])
"""

"""
#test api
covid_today = requests.get('https://covid19.th-stat.com/api/open/today')
covid_today.json()
#print (covid_today.json())
print("ติดเชื้อสะสม : ", (covid_today.json())['Confirmed'])
print("หายแล้ว : ", (covid_today.json())['Recovered'])
print("รักษาอยู่ใน รพ. : ", (covid_today.json())['Hospitalized'])
print("เสียชีวิต : ", (covid_today.json())['Deaths'])
"""

#Flask 
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
