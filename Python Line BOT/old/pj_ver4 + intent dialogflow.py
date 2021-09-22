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
    if intent_group_question_str == 'condition':
        answer_str = condition()
    elif intent_group_question_str == 'time_info':
        answer_str = time_info()
    elif intent_group_question_str == 'temp_info':
        answer_str = temp_info()
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

from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m/%d/%y, %H:%M:%S")

def condition(respond_dict): #ฟังก์ชั่นสำหรับบันทึกข้อมูล
    condition = str(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["condition.original"])
    print(condition)
    condition_str = str(condition)
    print(condition_str)
    sheet.insert_row([condition_str],2)
    answer_function = 'ทำการบันทึกว่า' + condition_str
    return answer_function

def time_info(respond_dict):
    #ตัวแปรเก็บค่า time
    time = float(respond_dict["queryResult"]["outputContexts"][0]["parameters"]["time.original"])
    print(time)
    time_str = str(time)
    print(time_str)
    sheet.insert_row([time_str],2)
    answer_function = 'ทำการบันทึก' + time_str
    return answer_function

def temp_info(respond_dict): #ฟังก์ชั่นสำหรับบันทึกข้อมูล
    temp = float(respond_dict["queryResult"]["outputContexts"][0]["parameters"]["condition.original"])
    print(temp)
    temp_str = str(temp)
    print(temp_info)
    sheet.insert_row([temp_str],2)
    answer_function = 'ทำการบันทึกว่า' + temp_str
    return answer_function

def covid_today():
    answer_function1 = 'text from python'
    c = requests.get('https://covid19.th-stat.com/api/open/today')
    c.json()
    data = json.loads(c.text)
    data = json.dumps(data)
    answer_function3 = data
    #answer_function2 = '{"line":{"text": ' + data + ',"type": "text"} }'
    return answer_function3

#Flask 
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
