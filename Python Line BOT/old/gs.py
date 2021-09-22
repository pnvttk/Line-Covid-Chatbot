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
condition = 'ไม่สบาย'
time = '12:30:00'
temp = '37.5'
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m/%d/%y, %H:%M:%S")
#write data
#cell=sheet.cell(row,column).value
#pprint(cell)
#sheet.update_cell(row,column,"แก้ไข")
sheet.insert_row([condition,time,temp,date_time],2)
#cell=sheet.cell(row,column).value
pprint(data)
