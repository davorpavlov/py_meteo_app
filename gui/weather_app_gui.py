import tkinter as tk
from tkinter import StringVar, ttk
from services.weather_data import refresh_data
from moduls.my_weather_module import getWeather



class WeatherAppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vremenska prognoza")
        self.geometry("500x650")
        
        self.style = ttk.Style()
        self.style.configure("Hot.TFrame", background="orange")
        self.style.configure("Moderate.TFrame", background="yellow")
        self.style.configure("Cold.TFrame", background="light blue")
        self.style.configure("LowPressure.TFrame", background="light green")
        self.style.configure("HighPressure.TFrame", background="red")
        self.style.configure("LowHumidity.TFrame", background="light yellow")
        self.style.configure("HighHumidity.TFrame", background="light pink")
        self.style.configure("Default.TFrame", background="white")

        self.frame1 = ttk.Frame(self, width=500, height=150, borderwidth=2, relief="solid")
        self.frame1.pack(fill="x", padx=10, pady=10)

        self.frame2 = ttk.Frame(self, width=500, height=150, borderwidth=2, relief="solid")
        self.frame2.pack(fill="x", padx=10, pady=10)

        self.frame3 = ttk.Frame(self, width=500, height=150, borderwidth=2, relief="solid")
        self.frame3.pack(fill="x", padx=10, pady=10)

        self.frame4 = ttk.Frame(self, width=500, height=150, borderwidth=2, relief="solid")
        self.frame4.pack(fill="x", padx=10, pady=10)

        self.label_city = tk.Label(self.frame1, text="Grad Zagreb", font=("Verdana", 14), anchor="w")
        self.label_city.pack(padx=10, pady=10, anchor="w") 

        self.label_general_data = tk.Label(self.frame1, text=getWeather(), font=("Verdana", 10), anchor="w", wraplength=400)
        self.label_general_data.pack(padx=10, pady=5, anchor="e", side="right")

        self.indoor_temp_var = tk.StringVar()
        self.label_indoor_temp = tk.Label(self.frame2, textvariable=self.indoor_temp_var, font=("Verdana", 12), anchor="w")
        self.label_indoor_temp.pack(padx=10, pady=5, anchor="w")

        self.outdoor_temp_var = tk.StringVar()
        self.label_outdoor_temp = tk.Label(self.frame2, textvariable=self.outdoor_temp_var, font=("Verdana", 12), anchor="w")
        self.label_outdoor_temp.pack(padx=10, pady=5, anchor="w")

        self.city_temp_var = tk.StringVar()
        self.label_city_temp = tk.Label(self.frame2, textvariable=self.city_temp_var, font=("Verdana", 12), anchor="w")
        self.label_city_temp.pack(padx=10, pady=5, anchor="w")

        self.indoor_pressure_var = tk.StringVar()
        self.label_indoor_pressure = tk.Label(self.frame3, textvariable=self.indoor_pressure_var, font=("Verdana", 12), anchor="w")
        self.label_indoor_pressure.pack(padx=10, pady=5, anchor="w")

        self.outdoor_pressure_var = tk.StringVar()
        self.label_outdoor_pressure = tk.Label(self.frame3, textvariable=self.outdoor_pressure_var, font=("Verdana", 12), anchor="w")
        self.label_outdoor_pressure.pack(padx=10, pady=5, anchor="w")

        self.outdoor_humidity_var = tk.StringVar()
        self.label_outdoor_humidity = tk.Label(self.frame4, textvariable=self.outdoor_humidity_var, font=("Verdana", 12), anchor="w")
        self.label_outdoor_humidity.pack(padx=10, pady=5, anchor="w")

        self.indoor_humidity_var = tk.StringVar()
        self.label_indoor_humidity = tk.Label(self.frame4, textvariable=self.indoor_humidity_var, font=("Verdana", 12), anchor="w")
        self.label_indoor_humidity.pack(padx=10, pady=5, anchor="w")

        self.button_refresh = tk.Button(self.frame4, text="Osvježi", font=("Verdana", 12), command=self.refresh_data)
        self.button_refresh.pack(padx=10, pady=10, anchor="e")

        self.clothing_icon_label = tk.Label(self.frame2)
        self.clothing_icon_label.pack(side="right", anchor="n")

        self.refresh_data()

    def refresh_data(self):
        refresh_data(self.indoor_temp_var, self.outdoor_temp_var, self.city_temp_var, self.indoor_pressure_var,
                    self.outdoor_pressure_var, self.outdoor_humidity_var, self.indoor_humidity_var, self.clothing_icon_label, self.frame2, self.frame3, self.frame4)
        
        

   
