import webbrowser
import os
import datetime
import wikipedia


def execute(query, speak):

# ---------------- INTERNET ---------------- #

    if "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open gmail" in query:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "open github" in query:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open stackoverflow" in query:
        webbrowser.open("https://stackoverflow.com")

    elif "open linkedin" in query:
        webbrowser.open("https://linkedin.com")

    elif "open netflix" in query:
        webbrowser.open("https://netflix.com")

    elif "open amazon" in query:
        webbrowser.open("https://amazon.in")

    elif "open flipkart" in query:
        webbrowser.open("https://flipkart.com")

    elif "open wikipedia" in query:
        webbrowser.open("https://wikipedia.org")


# ---------------- SEARCH ---------------- #

    elif "search" in query:
        query = query.replace("search", "")
        speak("Searching Google")
        webbrowser.open("https://google.com/search?q=" + query)

    elif "youtube search" in query:
        query = query.replace("youtube search", "")
        webbrowser.open(
            "https://youtube.com/results?search_query=" + query
        )


# ---------------- WIKIPEDIA ---------------- #

    elif "wikipedia" in query:
        topic = query.replace("wikipedia", "")
        speak("Searching Wikipedia")
        result = wikipedia.summary(topic, 2)
        speak(result)


# ---------------- MUSIC ---------------- #

    elif "play song" in query:
        song = query.replace("play song", "")
        speak("Playing " + song)

        webbrowser.open(
            "https://youtube.com/results?search_query=" + song
        )

    elif "play music" in query:
        webbrowser.open("https://music.youtube.com")


# ---------------- TIME & DATE ---------------- #

    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Current time is " + time)

    elif "date" in query:
        today = str(datetime.date.today())
        speak("Today's date is " + today)


# ---------------- APPLICATIONS ---------------- #

    elif "open notepad" in query:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in query:
        speak("Opening Calculator")
        os.system("calc")

    elif "open paint" in query:
        os.system("mspaint")

    elif "open command prompt" in query:
        os.system("start cmd")

    elif "open control panel" in query:
        os.system("control")

    elif "open task manager" in query:
        os.system("taskmgr")


# ---------------- SYSTEM CONTROL ---------------- #

    elif "shutdown computer" in query:
        speak("Shutting down computer")
        os.system("shutdown /s /t 5")

    elif "restart computer" in query:
        speak("Restarting computer")
        os.system("shutdown /r /t 5")

    elif "lock computer" in query:
        speak("Locking computer")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "sleep computer" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# ---------------- FILE MANAGEMENT ---------------- #

    elif "open downloads" in query:
        os.startfile(os.path.expanduser("~/Downloads"))

    elif "open documents" in query:
        os.startfile(os.path.expanduser("~/Documents"))

    elif "open desktop" in query:
        os.startfile(os.path.expanduser("~/Desktop"))


# ---------------- UTILITIES ---------------- #

    elif "ip address" in query:
        speak("Opening IP checker")
        webbrowser.open("https://whatismyipaddress.com")

    elif "internet speed test" in query:
        webbrowser.open("https://fast.com")

    elif "open maps" in query:
        webbrowser.open("https://maps.google.com")


# ---------------- ENTERTAINMENT ---------------- #

    elif "tell me a joke" in query:
        speak("Why do programmers prefer dark mode?")
        speak("Because light attracts bugs.")

    elif "hello jarvis" in query:
        speak("Hello. How can I assist you?")

    elif "who are you" in query:
        speak("I am Jarvis, your personal AI assistant.")


# ---------------- EXIT ---------------- #

    elif "exit jarvis" in query:
        speak("Goodbye")
        exit()


# ---------------- UNKNOWN COMMAND ---------------- #

    else:
        speak("Command not recognized")