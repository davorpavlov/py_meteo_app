import requests
import json
from tkinter import messagebox
from icons.clothing_icons import show_clothing_icon
from services.db_service import insert_weather_data


def refresh_data(indoor_temp_var, outdoor_temp_var, city_temp_var, indoor_pressure_var,
                 outdoor_pressure_var, outdoor_humidity_var, indoor_humidity_var, clothing_icon_label, frame2, frame3, frame4):
    # Dohvaćanje podataka o vremenskoj prognozi
    try:
        city = "Zagreb"
        web_api = f"http://api.weatherapi.com/v1/current.json?key=e341df510d2d416da26205427232204&q={city}&aqi=no"
        response = requests.get(web_api)
        data = json.loads(response.text)
        
        
        indoor_temp = data["current"]["temp_c"]+1
        outdoor_temp = data["current"]["temp_c"]
        city_temp = data["current"]["temp_c"]
        indoor_pressure = data["current"]["pressure_mb"]
        outdoor_pressure = data["current"]["pressure_mb"]
        outdoor_humidity = data["current"]["humidity"]
        indoor_humidity = data["current"]["humidity"]-10

        
        indoor_temp_var.set(f"Temperatura u kući: {indoor_temp} °C")
        outdoor_temp_var.set(f"Temperatura vani: {outdoor_temp} °C")
        city_temp_var.set(f"Temperatura u gradu: {city_temp} °C")
        indoor_pressure_var.set(f"Tlak zraka u kući: {indoor_pressure} hPa")
        outdoor_pressure_var.set(f"Tlak zraka vani: {outdoor_pressure} hPa")
        outdoor_humidity_var.set(f"Vlažnost zraka vani: {outdoor_humidity}%")
        indoor_humidity_var.set(f"Vlažnost zraka u kući: {indoor_humidity}%")

        
        temperature = int(city_temp)
        if temperature > 22:
            show_clothing_icon(clothing_icon_label, "icons\\pic\\kratki_rukavi.png")
        elif 12 <= temperature <= 22:
            show_clothing_icon(clothing_icon_label, "icons\\pic\\lagana_jakna.png")
        elif 0 <= temperature < 12:
            show_clothing_icon(clothing_icon_label, "icons\\pic\\zimska_jakna.png")
        else:
            show_clothing_icon(clothing_icon_label, "icons\\pic\\kapa_scarf_zimska_jakna.png")

        change_frame2_color(frame2, temperature)

        
        pressure = int(outdoor_pressure)
        humidity = int(outdoor_humidity)

        
        change_frame3_color(frame3, pressure)
        change_frame4_color(frame4, humidity)
        
        
        insert_weather_data("Zagreb", indoor_temp, outdoor_temp, indoor_pressure, outdoor_pressure, indoor_humidity, outdoor_humidity)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Greška", f"Greška prilikom dohvaćanja podataka: {str(e)}")
        
        
def change_frame2_color(frame, temperature):
    if temperature > 22:
        frame.configure(style="Hot.TFrame")
    elif 12 <= temperature <= 22:
        frame.configure(style="Moderate.TFrame")
    elif 0 <= temperature < 12:
        frame.configure(style="Cold.TFrame")
    else:
        frame.configure(style="Default.TFrame")

def change_frame3_color(frame, pressure):
    if pressure < 1000:
        frame.configure(style="LowPressure.TFrame")
    elif pressure > 1020:
        frame.configure(style="HighPressure.TFrame")
    else:
        frame.configure(style="Default.TFrame")

def change_frame4_color(frame, humidity):
    if humidity < 30:
        frame.configure(style="LowHumidity.TFrame")
    elif humidity > 70:
        frame.configure(style="HighHumidity.TFrame")
    else:
        frame.configure(style="Default.TFrame")
