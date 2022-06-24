from string import hexdigits
from tkinter import *



window = Tk()
window.title="Calculator"

e = Entry (window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def  button_click(number):
    return 

# Define button_s
button_0 = Button(window, text="0", padx= 40, pady= 20, command=Lambda: button_click(0))
button_1 = Button(window, text="1", padx= 40, pady= 20, command=Lambda: button_click(1))
button_2 = Button(window, text="2", padx= 40, pady= 20, command=Lambda: button_click(2))
button_3 = Button(window, text="3", padx= 40, pady= 20, command=Lambda: button_click(3))
button_4 = Button(window, text="4", padx= 40, pady= 20, command=Lambda: button_click(4))
button_5 = Button(window, text="5", padx= 40, pady= 20, command=Lambda: button_click(5))
button_6 = Button(window, text="6", padx= 40, pady= 20, command=Lambda: button_click(6))
button_7 = Button(window, text="7", padx= 40, pady= 20, command=Lambda: button_click(7))
button_8 = Button(window, text="8", padx= 40, pady= 20, command=Lambda: button_click(8))
button_9 = Button(window, text="9", padx= 40, pady= 20, command=Lambda: button_click(9))
button_Plus = Button(window, text="+", padx= 40, pady= 20, command=Lambda: button_click())
button_Eq = Button(window, text="=", padx= 91, pady= 20, command=Lambda: button_click())
button_Clear = Button(window, text="Clear", padx= 79, pady= 20, command=Lambda: button_click())

# Putting the number on the scree
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_Clear.grid(row=4, column=1, columnspan=2)
button_Plus.grid(row=5, column=0)
button_Eq.grid(row=5, column=1, columnspan=2)

#Start the GUI event loop
window.mainloop()