import tkinter as tk
from weather_core import get_location_id, get_weather, get_weather_states_icons, analyse_weather, present_weather_daily


def present_weather():
    city = entry['City name'].get()
    city_id = get_location_id(city)
    weather_data = get_weather(city_id)
    forecast_range = int(entry['Forecast range'].get())
    details = True
    for i in range(forecast_range):
        text = present_weather_daily(weather_data, i, details)
        result_label = tk.Label(master=window, text=text)
        result_label.grid(row=0, column=i+1)

    return city_id


window = tk.Tk()
window.title('GUI for weather forecast display')

window.columnconfigure([0, 1, 2], weight=1, minsize=150)

frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frame.grid(row=0, column=0)

frame.columnconfigure(0, weight=1, minsize=75)
frame.columnconfigure(1, weight=1, minsize=150)

labels = ['City name', 'Forecast range']
entry = {}

for i, lab in enumerate(labels):
    label = tk.Label(master=frame, text=f'{lab}:')
    label.grid(row=i, column=0)
    entry[lab] = (tk.Entry(master=frame, bg="white", fg="blue"))
    entry[lab].grid(row=i, column=1, sticky="ew")

frm_buttons = tk.Frame(master=frame)
frm_buttons.grid(row=2, column=0)

btn_submit = tk.Button(master=frm_buttons, text="Show forecast", command=present_weather)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

window.mainloop()
