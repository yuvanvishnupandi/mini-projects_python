import tkinter as tk
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speech speed

root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x500")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
        label_status.config(text="Good Morning!")
    elif hour < 18:
        speak("Good afternoon!")
        label_status.config(text="Good Afternoon!")
    else:
        speak("Good evening!")
        label_status.config(text="Good Evening!")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        label_status.config(text="Listening...")
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        label_status.config(text="Processing...")
        process_query(query)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        label_status.config(text="Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Sorry, I'm having trouble.")
        label_status.config(text="Sorry, I’m having trouble.")

def stop_listening():
    speak("Stopping listening. Have a great day!")
    label_status.config(text="Stopped")
    root.quit()
    
def process_query(query):
    query = query.lower()

    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(results)
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, results)

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, f"The time is {current_time}")

    elif "play music" in query:
        speak("Playing music")
        webbrowser.open("https://www.spotify.com")

    else:
        speak("Sorry, I didn’t understand. Let me search for it.")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    label_status.config(text="Ready")

def clear_text():
    text_display.delete(1.0, tk.END)
    label_status.config(text="Ready")

label = tk.Label(root, text="Voice Assistant", font=("Arial", 20))
label.pack(pady=20)

label_status = tk.Label(root, text="Ready", font=("Arial", 12))
label_status.pack()

text_display = tk.Text(root, height=8, width=40)
text_display.pack(pady=10)

button_listen = tk.Button(root, text="Start Listening", command=take_command, width=20, height=2)
button_listen.pack(pady=10)

button_stop = tk.Button(root, text="Stop Listening", command=stop_listening, width=20, height=2)
button_stop.pack(pady=10)

button_clear = tk.Button(root, text="Clear Text", command=clear_text, width=20, height=2)
button_clear.pack(pady=10)

greet()
root.mainloop()