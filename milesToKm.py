from tkinter import *

def button_clicked():
    result = float(entry.get()) * 1.609
    result_label.config(text= f"{result}")

window = Tk()
window.title("Miles to km converter")
window.config(padx= 15, pady= 15)

entry = Entry(width=8)
entry.grid(row=0, column=3)

miles_label = Label(text="miles", font=("Calibri",11))
miles_label.grid(row=0, column=5)

label = Label(text="is equal to ", font=("Calibri",11))
label.grid(row=1,column=0)

result_label = Label(text=" ", font=("Calibri",11, "bold"))
result_label.grid(row=1, column=3)

km_label = Label(text=" km", font=("Calibri",11))
km_label.grid(row=1,column=5)

button = Button(text="Convert",command=button_clicked)
button.grid(row=2, column= 3)




window.mainloop()