#gee python project

# importing modules

import json
import requests
from tkinter import *
from PIL import ImageTk,Image

# Required Details
root = Tk()
root.geometry("320x320")
root.title("Weather App")
root.configure(bg='black')

# for images

img = ImageTk.PhotoImage(Image.open('um.png'))
panel = Label(root,image=img)
panel.place(x=112,y=3)

lable_0 = Label(root,text="Weather App",width = 20,bg='black',font=("bold",20),fg='white')
lable_0.place(x=0,y=93)

city_names = StringVar()
entry_1 = Entry(root,textvariable=city_names)
city_names.set("Enter City Here")
entry_1.place(x=102,y=140)



lable_2 = Label(root,text="Temprature : ",width = 20,bg='black',font=("bold",10),fg='blue')
lable_2.place(x=45,y=220)

lable_3 = Label(root,text="Pressure : ",width = 20,bg='black',font=("bold",10),fg='blue')
lable_3.place(x=45,y=240)

lable_5 = Label(root,text="Humidity : ",width = 20,bg='black',font=("bold",10),fg='blue')
lable_5.place(x=45,y=260)


lable_temp = Label(root,text="...",width = 5,bg='black',font=("bold",10),fg='blue')
lable_temp.place(x=160,y=220)

lable_pres = Label(root,text="...",width = 5,bg='black',font=("bold",10),fg='blue')
lable_pres.place(x=160,y=240)

lable_humi = Label(root,text="...",width = 5,bg='black',font=("bold",10),fg='blue')
lable_humi.place(x=160,y=260)

#unit
lable_humi1 = Label(root,text="%",width = 5,bg='black',font=("bold",10),fg='blue')
lable_humi1.place(x=200,y=260)

lable_Utemp = Label(root,text="C",width = 5,bg='black',font=("bold",10),fg='blue')
lable_Utemp.place(x=200,y=220)

lable_Upres = Label(root,text="Pa",width = 5,bg='black',font=("bold",10),fg='blue')
lable_Upres.place(x=200,y=240)



# api config
def getTemp():

    api_key = "8280aeb47d8dd85caf5984c97d2f6947"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = entry_1.get()
    complete_url = base_url+"appid="+api_key+"&q="+city_name 

# module response get

    response = requests.get(complete_url)
    x=response.json()

    if["cod"] !='404':
        y = x["main"]
        current_temprature = y["temp"]
        current_temprature = current_temprature - 273.15    #แปลงหน่วย K เป็น C
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        

        lable_pres.configure(text=current_pressure)
        lable_temp.configure(text=current_temprature)
        lable_humi.configure(text=current_humidity)
       
    else:
        lable_pres.configure(text="Err")
        lable_temp.configure(text="Err")
        lable_humi.configure(text="Err")
        

Button(root,text="Submit",width=10,bg='brown',fg='white',command=getTemp).place(x=122,y=170)

lable_unit = Label(root,text="Temprature in C And Pressure in Pa",width = 40,bg='black',font=("bold",10),fg='white')
lable_unit.place(x=5,y=290)

mainloop()