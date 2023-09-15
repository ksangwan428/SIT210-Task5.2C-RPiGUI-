# Import necessary libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

#2210994801

# Setting up the Raspberry Pi pin mode to BCM
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
# Define LEDs with their BCM pin numbers
red = LED(14)
green = LED(15)
blue = LED(18)

### GUI DEFINITIONS ###
# Setting up the main window
win = Tk()
win.title("Car LED Controller")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

# Canvas to draw the car representation
canvas = Canvas(win, width=400, height=200, bg="white")
canvas.grid(row=0, column=0, columnspan=5)

# Drawing car elements on the canvas
canvas.create_rectangle(50, 100, 350, 180, fill="gray")  # Car body
canvas.create_rectangle(80, 110, 320, 140, fill="blue")  # Car windows
canvas.create_oval(70, 170, 110, 200, fill="black")      # Left wheel
canvas.create_oval(290, 170, 330, 200, fill="black")     # Right wheel

### Event Functions ###
# Define behavior for the Red LED button
def RedLed():
    if red.is_lit:
        red.off()
        canvas.itemconfig(red_light, fill="gray")
    else:
        red.on()
        green.off()
        blue.off()
        canvas.itemconfig(red_light, fill="red")

# Define behavior for the Green LED button
def GreenLed():
    if green.is_lit:
        green.off()
        canvas.itemconfig(green_light, fill="gray")
    else:
        green.on()
        red.off()
        blue.off()
        canvas.itemconfig(green_light, fill="green")

# Define behavior for the Blue LED button
def BlueLed():
    if blue.is_lit:
        blue.off()
        canvas.itemconfig(blue_light, fill="gray")
    else:
        blue.on()
        red.off()
        green.off()
        canvas.itemconfig(blue_light, fill="blue")

# Define behavior when the application is closed
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Drawing LED representations on the canvas
red_light = canvas.create_oval(70, 110, 110, 140, fill="gray")
green_light = canvas.create_oval(160, 110, 200, 140, fill="gray")
blue_light = canvas.create_oval(290, 110, 330, 140, fill="gray")

# Creating the radio buttons for LED control
Radiobutton(win, text='Red LED', font=myFont, command=RedLed, bg='red', height=1, width=24).grid(row=1, column=0)
Radiobutton(win, text='Green LED', font=myFont, command=GreenLed, bg='green', height=1, width=24).grid(row=1, column=1)
Radiobutton(win, text='Blue LED', font=myFont, command=BlueLed, bg='blue', height=1, width=24).grid(row=1, column=2)

# Exit button definition
exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=1, column=3)

# Attach close function to window close button event
win.protocol("WM_DELETE_WINDOW", close)  

# Start the GUI event loop
win.mainloop()
