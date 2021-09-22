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

#show data
#pprint(data)
"""
#-----------------------------write data
cell=sheet.cell(4,2).value
pprint(cell)
sheet.update_cell(4,2,"แก้ไข")
cell=sheet.cell(4,2).value
pprint(cell)
"""

#-------------------------------fire base
"""
def firebase(): #testing
    from random import randint
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore
    cred = credentials.Certificate("cerds.json")
    firebase_admin.initilize_app(cred)
"""

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
    elif intent_group_question_str == 'ทดสอบ':
        answer_str = test_text()
    elif intent_group_question_str == 'หิวจัง':
        answer_str = menu_recormentation()
    else: answer_str = "Error"

    #สร้างการแสดงของ dict 
    answer_from_bot = {"fulfillmentText": answer_str}
    
    #แปลงจาก dict ให้เป็น JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4) 
    
    return answer_from_bot

def menu_recormentation(): #ฟังก์ชั่นสำหรับเมนูแนะนำ
    menu_name = 'ข้าวขาหมู'
    answer_function = menu_name + ' สิ น่ากินนะ'
    return answer_function
    
def test_text():
    test_text = 'ข้อความจาก python'   
    answer_function =  test_text
    return answer_function

def save_data(): #ฟังก์ชั่นสำหรับบันทึกข้อมูล
    ans1 = ' กรุณาบอกเวลาล่าสุดที่ได้ตรวจวัดอุณหภูมิ เช่น 09:00 หรือ "-", "จำไม่ได้"'   
    answer_function = 'จะเริ่มทำการบันทึกข้อมูล' + ans1
    return answer_function

def covid_today():
    answer_function = 'text from python'
    r = requests.get('https://covid19.th-stat.com/api/open/today')
    r.json()
    #from pprint import pprint
    #pprint(r.json())
    answer_c = 'กำลังแสดงข้อมูล' #+ r.text()
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
    return answer_function

#Flask 
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
