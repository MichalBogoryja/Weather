import tkinter as tk
from weather_core import get_location_id, get_weather, \
    get_weather_states_icons, present_weather_daily, analyse_weather, \
    present_outline_weather

result_label = []
img = []
canvas = []


def present_weather(data):
    global result_label
    clear()
    city = data['City name'].get()
    if not city:
        city = 'Warsaw'
    while True:
        if city[-1] == ' ':
            city = city[:-1]
        else:
            break
    city_id = get_location_id(city)
    weather_data = get_weather(city_id)
    forecast_range = data['Forecast range'].get()
    if not forecast_range:
        forecast_range = 3
    else:
        forecast_range = int(forecast_range)
    if details.get() == 1:
        detailed = True
    else:
        detailed = False
    if metrics.get() == 2:
        units = False
    else:
        units = True

    print(outline_weather(weather_data))

    daily_weather(forecast_range, weather_data, detailed, units)

    btn_no_details.select()
    btn_metric.select()

    return result_label


def daily_weather(forecast_range, data, detail, units):
    for day in range(forecast_range):
        text = present_weather_daily(data, day, detail, units)
        print(text)
        result_label.append(tk.Label(master=window, text=text))
        result_label[day+1].grid(row=1, column=day+2)
        show_image(day, data)


def outline_weather(data):
    global result_label
    forecast_data = present_outline_weather(data)
    result_label.append(tk.Label(master=window, text=forecast_data))
    result_label[0].grid(row=1, column=1)
    return forecast_data


def clear():
    global result_label, img, canvas
    for i in range(len(result_label)):
        result_label[i].destroy()
    for i in range(len(canvas)):
        canvas[i].destroy()
    result_label = []
    img = []
    canvas = []


def show_image(col, data):
    global img
    global canvas
    weather_data = analyse_weather(data, col)
    weather_state = weather_data.state_abbr
    img_dir = get_weather_states_icons(weather_state)
    canvas.append(tk.Canvas(master=window, width=100, height=80, bg="#ADD8E6"))
    canvas[len(canvas)-1].grid(row=0, column=col+2, stick="nsew")
    img.append(tk.PhotoImage(file=f'{img_dir}/{weather_state}.jpg'))
    canvas[len(canvas)-1].create_image(64, 45, image=img[col])
    pass


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

frm_buttons = tk.Frame(master=frame)
frm_buttons.grid(row=(len(labels)), column=0)

details = tk.IntVar()

btn_details = tk.Radiobutton(master=frm_buttons, text='Details',
                             variable=details, value=1)
btn_details.grid(row=0, column=0)

btn_no_details = tk.Radiobutton(master=frm_buttons, text='No details',
                                variable=details, value=2)
btn_no_details.grid(row=0, column=1)

metrics = tk.IntVar()

btn_metric = tk.Radiobutton(master=frm_buttons, text='Metric',
                            variable=metrics, value=1)
btn_metric.grid(row=1, column=0)

btn_imperial = tk.Radiobutton(master=frm_buttons, text='Imperial',
                              variable=metrics, value=2)
btn_imperial.grid(row=1, column=1)

btn_submit = tk.Button(master=frame, text="Show forecast",
                       command=lambda: present_weather(entry))
btn_submit.grid(row=(len(labels)), column=1)

window.mainloop()
