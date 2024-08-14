import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        # Entry for city input
        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.pack(pady=10)

        # Button to fetch weather
        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        # Label to display weather information
        self.weather_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.weather_label.pack(pady=20)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showwarning("Warning", "Please enter a city.")
            return
        
        api_key = 'YOUR_API_KEY'  # Replace with your API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        try:
            response = requests.get(url)
            data = response.json()
            if data['cod'] == 200:
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                self.weather_label.config(text=f"Weather: {weather_description}\nTemperature: {temperature} °C")
            else:
                messagebox.showerror("Error", f"Error: {data['message']}")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching weather data: {e}")

# Create the main tkinter window
root = tk.Tk()

# Create an instance of WeatherApp
app = WeatherApp(root)

# Run the tkinter main loop
root.mainloop()
