import tkinter as tk
import math
import random
import threading
import speech_recognition as sr
import pyttsx3
from commands import execute

engine = pyttsx3.init()
engine.setProperty('rate',170)

angle = 0
scan_angle = 0

# ---------------- SPEAK ---------------- #

def speak(text):

    console.insert(tk.END,"Jarvis: "+text+"\n")
    console.see(tk.END)

    engine.say(text)
    engine.runAndWait()


# ---------------- LISTEN ---------------- #

def take_command():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        console.insert(tk.END,"Listening...\n")
        root.update()

        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        console.insert(tk.END,"You: "+query+"\n")

    except:
        return "none"

    return query.lower()


# ---------------- JARVIS LOOP ---------------- #

def jarvis_loop():

    speak("Jarvis online")

    while True:

        query = take_command()

        if query == "none":
            continue

        if "exit jarvis" in query:
            speak("Shutting down")
            break

        execute(query,speak)


def start_jarvis():

    threading.Thread(target=jarvis_loop).start()


# ---------------- BOOT ANIMATION ---------------- #

boot_lines = [
"Initializing Systems...",
"Loading AI Core...",
"Activating Voice Modules...",
"Connecting Command Network...",
"Jarvis Ready"
]

def boot():

    for line in boot_lines:

        console.insert(tk.END,line+"\n")
        root.update()
        root.after(500)

    speak("Jarvis system ready")


# ---------------- HUD ANIMATION ---------------- #

def draw_hud():

    global angle, scan_angle

    canvas.delete("all")

    cx = 200
    cy = 150

    # OUTER RING
    for i in range(0,360,8):

        a = math.radians(i + angle)

        x = cx + math.cos(a)*90
        y = cy + math.sin(a)*90

        canvas.create_oval(x-2,y-2,x+2,y+2,fill="#00ffff")

    # MIDDLE RING
    for i in range(0,360,12):

        a = math.radians(i - angle)

        x = cx + math.cos(a)*65
        y = cy + math.sin(a)*65

        canvas.create_oval(x-3,y-3,x+3,y+3,fill="#00ffff")

    # INNER RING
    for i in range(0,360,18):

        a = math.radians(i + angle*2)

        x = cx + math.cos(a)*40
        y = cy + math.sin(a)*40

        canvas.create_oval(x-3,y-3,x+3,y+3,fill="#00ffff")

    # CENTER CORE
    canvas.create_oval(cx-20,cy-20,cx+20,cy+20,
                       outline="#00ffff",width=2)

    # RADAR SCAN LINE
    scan = math.radians(scan_angle)

    x = cx + math.cos(scan)*95
    y = cy + math.sin(scan)*95

    canvas.create_line(cx,cy,x,y,
                       fill="#00ffff",
                       width=2)

    angle += 2
    scan_angle += 4

    root.after(40,draw_hud)


# ---------------- VOICE VISUALIZER ---------------- #

def draw_wave():

    wave.delete("all")

    for i in range(35):

        h = random.randint(10,60)

        wave.create_line(
            i*10,70,
            i*10,70-h,
            fill="#00ffff",
            width=3
        )

    root.after(120,draw_wave)


# ---------------- GUI ---------------- #

root = tk.Tk()

root.title("JARVIS AI SYSTEM")
root.geometry("650x500")
root.configure(bg="black")

title = tk.Label(
root,
text="JARVIS AI HUD",
font=("Orbitron",22),
fg="#00ffff",
bg="black"
)

title.pack(pady=10)


canvas = tk.Canvas(
root,
width=400,
height=300,
bg="black",
highlightthickness=0
)

canvas.pack()


wave = tk.Canvas(
root,
width=400,
height=80,
bg="black",
highlightthickness=0
)

wave.pack()


console = tk.Text(
root,
height=7,
width=70,
bg="black",
fg="#00ffff",
font=("Consolas",10)
)

console.pack(pady=6)


btn = tk.Button(
root,
text="ACTIVATE JARVIS",
font=("Arial",11),
bg="#00ffff",
command=start_jarvis
)

btn.pack(pady=8)


boot()

draw_hud()
draw_wave()

root.mainloop()