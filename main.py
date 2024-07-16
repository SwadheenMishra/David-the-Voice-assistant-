import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from datetime import datetime


def speak(text: str) -> None:
    tts = gTTS(text, tld='us', lang='en', slow=False)
    tts.save("temp.mp3")
    playsound("temp.mp3")
    os.remove("temp.mp3")

def take_Command() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def main():
    speak('System Online!')
    while True:
        query = take_Command().lower()

        if 'good night' in query:
            speak('Good Night Sir!')
        elif 'introduce yourself' in query:
            speak('I am an AI built to help with day to day tasks!')
        elif 'hai' in query:
            speak('Hello! How may i assist you?')
        elif 'hello' in query:
            speak('Hi! how can i help you today?')
        elif 'what time' or 'whats the time' or 'what time is it' in query:
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            speak(f'The time is {time}')

if __name__ == '__main__':
    main()
        
