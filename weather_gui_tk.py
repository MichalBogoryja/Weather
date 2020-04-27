import tkinter as tk
from weather_core import get_location_id, get_weather, get_weather_states_icons, analyse_weather, present_weather_daily

result_label = []


def present_weather(data):
    global result_label
    clear()
    city = data['City name'].get()
    city_id = get_location_id(city)
    weather_data = get_weather(city_id)
    forecast_range = int(data['Forecast range'].get())
    if details.get() == 1:
        detailed = True
    else:
        detailed = False
    for i in range(forecast_range):
        text = present_weather_daily(weather_data, i, detailed)
        result_label.append(tk.Label(master=window, text=text))
        result_label[i].grid(row=0, column=i+1)
    btn_no_details.select()

    return result_label


def clear():
    global result_label
    for i in range(len(result_label)):
        result_label[i].destroy()
    result_label = []


window = tk.Tk()
window.title('GUI for weather forecast display')

window.columnconfigure([0, 1, 2], weight=1, minsize=150)

frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frame.grid(row=0, column=0)

frame.columnconfigure(0, weight=1, minsize=75)
frame.columnconfigure(1, weight=1, minsize=150)

labels = ['City name', 'Forecast range']
entry = {}
label = []

for i, lab in enumerate(labels):
    label.append(tk.Label(master=frame, text=f'{lab}:'))
    label[i].grid(row=i, column=0)
    entry[lab] = (tk.Entry(master=frame, bg="white", fg="blue"))
    entry[lab].grid(row=i, column=1, sticky="ew")

# print(type(label))
# print(label)
# print(label[0])
# label[0].destroy()
# print(label)


frm_buttons = tk.Frame(master=frame)
frm_buttons.grid(row=(len(labels)), column=0)

details = tk.IntVar()

btn_details = tk.Radiobutton(master=frm_buttons, text='Details', variable=details, value=1)
btn_details.pack(side=tk.LEFT, padx=5, ipadx=5)

btn_no_details = tk.Radiobutton(master=frm_buttons, text='No details', variable=details, value=2)
btn_no_details.pack(side=tk.LEFT, padx=5, ipadx=5)

btn_submit = tk.Button(master=frame, text="Show forecast", command=lambda: (result_label, present_weather(entry)))
print(btn_submit)
btn_submit.grid(row=(len(labels)), column=1)

# result_label = present_weather(entry)

window.mainloop()
