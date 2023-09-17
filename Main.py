# Import necessary libraries
import RPi.GPIO as GPIO, time
from tkinter import *
from tkinter import ttk

#2210994801

# Initialize the main window for the GUI application
window = Tk()
window.geometry("400x150")
window.title("String to Morse Code")

# Create a frame within the main window to represent the radio
radio_body = Frame(window, bg='black', bd=5)
radio_body.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.95, anchor='center')

# Label to act as the radio's display
radio_display = Label(radio_body, bg='grey', font=('Arial', 12), text="Morse Code Radio")
radio_display.pack(pady=5)

# Styling for the tkinter widgets
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 10), background='sky blue')
style.configure('TEntry', font=('Helvetica', 10), padding=5)

# Variable to capture text input from the user
textInput = StringVar()

# GPIO settings for LED
LED = 18
unit = 0.5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

# Morse code functions for dot, dash, and character spacing

def dot():
    # Signal a 'dot' in morse code with LED
    GPIO.output(LED, True)
    time.sleep(unit)
    GPIO.output(LED, False)
    time.sleep(unit)

def dash():
    # Signal a 'dash' in morse code with LED
    GPIO.output(LED, True)
    time.sleep(unit*3)
    GPIO.output(LED, False)
    time.sleep(unit)

def newChar():
    # Pause to signify the end of a character
    time.sleep(unit*2)



# functions for each letter of the alphabet
# calls the dot, dash and newChar functions in the relevant order
def A():
	dot()
	dash()

def B():
	dash()
	dot()
	dot()
	dot()
	
def C():
	dash()
	dot()
	dash()
	dot()

def D():
	dash()
	dot()
	dot()
	
def E():
	dot()

def F():
	dot()
	dot()
	dash()
	dot()

def G():
	dash()
	dash()
	dot()
	
def H():
	dot()
	dot()
	dot()
	dot()
	
def I():
	dot()
	dot()
	
def J():
	dot()
	dash()
	dash()
	dash()
	
def K():
	dash()
	dot()
	dash()
	
def L():
	dot()
	dash()
	dot()
	dot()
	
def M():
	dash()
	dash()
	
def N():
	dash()
	dot()
	
def O():
	dash()
	dash()
	dash()
	
def P():
	dot()
	dash()
	dash()
	dot()
	
def Q():
	dash()
	dash()
	dot()
	dash()
	
def R():
	dot()
	dash()
	dot()
	
def S():
	dot()
	dot()
	dot()

def T():
	dash()
	
def U():
	dot()
	dot()
	dash()
	
def V():
	dot()
	dot()
	dot()
	dash()
	
def W():
	dot()
	dash()
	dash()
	
def X():
	dash()
	dot()
	dot()
	dash()

def Y():
	dash()
	dot()
	dash()
	dash()
	
def Z():
	dash()
	dash()
	dot()
	dot()

# iterates through the text input and calls the appropriate function for each letter
def convertToCode():
	MorseText = textInput.get()
	if len(MorseText) > 12:
		return
	for i in MorseText:
		if i.upper() == "A":
			A()
		elif i.upper() == "B":
			B()
		elif i.upper() == "C":
			C()
		elif i.upper() == "D":
			D()
		elif i.upper() == "E":
			E()	
		elif i.upper() == "F":
			F()
		elif i.upper() == "G":
			G()
		elif i.upper() == "H":
			H()
		elif i.upper() == "I":
			I()
		elif i.upper() == "J":
			J()
		elif i.upper() == "K":
			K()
		elif i.upper() == "L":
			L()
		elif i.upper() == "M":
			M()
		elif i.upper() == "N":
			N()
		elif i.upper() == "O":
			O()
		elif i.upper() == "P":
			P()
		elif i.upper() == "Q":
			Q()
		elif i.upper() == "R":
			R()
		elif i.upper() == "S":
			S()
		elif i.upper() == "T":
			T()
		elif i.upper() == "U":
			U()
		elif i.upper() == "V":
			V()
		elif i.upper() == "W":
			W()
		elif i.upper() == "X":
			X()
		elif i.upper() == "Y":
			Y()
		elif i.upper() == "Z":
			Z()

# GUI elements
textEntry = ttk.Entry(radio_body, width=20, textvariable=textInput)
convertButton = ttk.Button(radio_body, text="Convert to Morse Code", command=convertToCode)

textEntry.pack(pady=5)
convertButton.pack(pady=5)

window.mainloop()
