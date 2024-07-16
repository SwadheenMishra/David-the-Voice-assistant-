import os
import tkinter as tk
from tkinter import scrolledtext
from gtts import gTTS
from playsound import playsound

# Function to convert text to speech
def speak_text(text: str) -> None:
    tts = gTTS(text, lang='en')
    tts.save("temp.mp3")
    playsound("temp.mp3")
    os.remove("temp.mp3")

def main():
    speak_text('test - Hack CLub') # its working!!

if __name__ == '__main__':
    main()
        
