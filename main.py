import speech_recognition as sr
from datetime import datetime
import random
import elevenlabs
import elevenlabs.client

# ===this is just to hide my api key===
import API

APIKEY = API.get_api_key()
# ====================================== 



def speak(text: str) -> None:
    global APIKEY

    client = elevenlabs.client.ElevenLabs(api_key=APIKEY)
    audio = client.generate(text=text,voice=elevenlabs.Voice(
            voice_id='TX3LPaxmHKxFdv7VOQHJ',
            settings=elevenlabs.VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        ))

    elevenlabs.play(audio)

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
    # resposeHello = ['Hi!']

    speak('System Online.')
    
    while True:
        query = take_Command().lower()

        if 'hello' in query:
            speak('Hi! How may i assist you?')
        elif 'hai' in query:
            speak('Hello! How can i help you?')
        elif 'introduce yourself' in query:
            speak('My name is david and i am an AI built to help with day to day tasks!')
        
        

if __name__ == '__main__':
    main()
