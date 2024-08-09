import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from core import fare_predict, plot_all

# window
window = ThemedTk(theme="black")
window.configure(background='black')
# title
window.title('Taxi Fare Calculator')
# var
weekday_var = tk.StringVar()
time_var = tk.StringVar()
dis_var = tk.StringVar()

style = ttk.Style()
style.configure("B.TFrame", foreground="grey", background="black")

# widgets
title_label = ttk.Label(master=window, text= "Taxi fare", font= 'Calibri 24',background='black')
title_label.pack()

# input fields
# weekdays
input_frame_0 = ttk.Frame(master=window,style="B.TFrame")
input_frame_0.pack()

time_label = ttk.Label(master=input_frame_0, text= "Weekday", font= 'Calibri 16',background='black')
entry_day = ttk.Entry(master=input_frame_0, textvariable= weekday_var,width=50,background='black')
time_label.pack(side= 'left', padx= 10,pady=5)
entry_day.insert(0, "Monday - Sunday = 0 - 6")
entry_day.pack(side= 'right', padx= 10)

# hours
input_frame_1 = ttk.Frame(master=window,style='B.TFrame')
input_frame_1.pack()
time_label = ttk.Label(master=input_frame_1, text= "Hour", font= 'Calibri 16',background='black')
entry_time = ttk.Entry(master=input_frame_1, textvariable= time_var,width=50,background='black')
entry_time.insert(0,"hour of day")
time_label.pack(side= 'left', padx= 29,pady=5)
entry_time.pack(side= 'right')

# distance
input_frame_2 = ttk.Frame(master=window,style='B.TFrame')
input_frame_2.pack()
dis_label = ttk.Label(master=input_frame_2, text= "Dis", font= 'Calibri 16',background='black')
entry_dis = ttk.Entry(master=input_frame_2, textvariable= dis_var,width=50,background='black')
entry_dis.insert(0,"miles")
dis_label.pack(side= 'left', padx= 36,pady=5)
entry_dis.pack(side= 'right')

# Results
frame_fare = ttk.Frame(master=window,style='B.TFrame')
frame_fare.pack()
fare_label = ttk.Label(master=frame_fare, text= "Fare", font= 'Calibri 16',background='black').pack(side= 'left', padx= 10,pady=5)
fare_display = ttk.Label(master=frame_fare, font= 'Calibri 16', text="$",background='black')
fare_display.pack(side='right')

# Button
def submit():
    weekday= float(weekday_var.get())
    time= float(time_var.get())
    dis = float(dis_var.get())

    total_fare = fare_predict([weekday,time,dis])
    global fare_display
    fare_display.config(text= "{:.2f}".format(total_fare[0]) + '$')

button_frame= ttk.Frame(master=window,style='B.TFrame').pack()
submit_button = ttk.Button(text="Result", command=submit, master=button_frame,compound='center')
submit_button.pack(side='left', anchor='e', expand=True, padx=10)
graph_button = ttk.Button(text="Relation graphs", command= plot_all, master=button_frame, compound='center')
graph_button.pack(side='right', anchor='w', expand=True, padx=10)

# loop
window.mainloop()