from tkinter import *
from tkinter import ttk
import time
import requests
import json
import screeninfo

screen_info  = screeninfo.get_monitors()[0]
# print(screen_info)
screen_w = screen_info.width
screen_h = screen_info.height
# from indian_cities.dj_city import cities 
# print(cities)
# this is for getting the indian cities

def get_weather( ):
    api_key = "45eddc0b6b7f0b4dc2ef4cc79365ce94"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city = City_name.get()
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)

    if weather_data["cod"] != "404":
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        Weather_type_1 .config(text=weather_data['weather'][0]['main'])
        weather_dsc_1.config(text=description )
        prs_1.config(text= str(round((wind_speed)*(3.6),2)) + ' km/hr')
        Temp_1.config(text=str(temperature) + ' C')
        
        # date_time = weather_data['dt']
        # print(weather_data)
        # print(f"Weather in {city}:")
        # print(f"Temperature: {temperature}°C")
        # print(f"Description: {description}")
        # print(f"Humidity: {humidity}%")
        # print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found!")


 
win = Tk()
win.title('Weather App Using python')
win.config(bg='#00FFFF')
win.geometry(str(screen_w )+'x' + str(screen_h))
list_city = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


name_label = Label(win,text='Python Weather App',font=('',30))
name_label.place(x=(screen_w/2 - 300),y=50,height=60,width=600)
City_name = StringVar()
com = ttk.Combobox(win,text='Python Weather App',font=('',14),values=list_city,textvariable=City_name)
com.place(x=(screen_w/2- 250 ),y=130,height=30,width=500)

Weather_type = Label(win,text='weather type',font=('',20))
Weather_type.place(x=(screen_w/2 - 400),y=200,height=40,width=400)
Weather_type_1 = Label(win,text='',font=('',20))
Weather_type_1.place(x=(screen_w/2 +100),y=200,height=40,width=400)


weather_dsc = Label(win,text='weather description',font=('',20))
weather_dsc.place(x=(screen_w/2 - 400),y=270,height=50,width=400)
weather_dsc_1 = Label(win,text='',font=('',20))
weather_dsc_1.place(x=(screen_w/2 +100),y=270,height=50,width=400)
Temp = Label(win,text='Current Temprature',font=('',20))
Temp.place(x=(screen_w/2 - 400),y=350,height=40,width=400)

Temp_1 = Label(win,text='temp',font=('',25))
Temp_1.place(x=(screen_w/2 +100),y=350,height=40,width=400)

prs = Label(win,text='Wind Speed',font=('',20))
prs.place(x=(screen_w/2 - 400),y=430,height=50,width=400)

prs_1 = Label(win,text='p',font=('',20))
prs_1.place(x=(screen_w/2 +100),y=430,height=50,width=400)






Search_button  = Button(win,text='Search',font=('',24),command=get_weather)
Search_button.place(x=(screen_w/2 -30),y=500,height=50,width=150)


win.mainloop()