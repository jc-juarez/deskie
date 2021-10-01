import tkinter as tk
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id) 

def sayHi():
    name = textBox1.get()
    myNew["text"] = "Hello sir " + name 
    engine.say(myNew["text"])
    engine.say("What do you need?")
    engine.runAndWait()

window = tk.Tk()
window.geometry("400x300")
myLabel = tk.Label(window, text = "Deskie", bg = "#F8A43A", fg = "#FFFFFF")
myLabel.pack()

textBox1 = tk.Entry(window)
textBox1.pack()

button1 = tk.Button(window, text = "Start Deskie", command = lambda: sayHi())

button1.pack()

myNew = tk.Label(window)
myNew.pack()

window.mainloop()

