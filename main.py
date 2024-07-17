import speech_recognition as sr
from datetime import datetime
import pyttsx3
import random
import elevenlabs
import elevenlabs.client

# ===this is just to hide my api key===
import API


client = None
Use11LabsApi = False

if not Use11LabsApi:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 190)
else:
    APIKEY = API.get_api_key()
    client = elevenlabs.client.ElevenLabs(api_key=APIKEY)

    
# ====================================== 

responses = {
    'hello': [
        'Hi! How may I assist you today?',
        'Hello! What can I do for you?',
        'Greetings! How can I help you today?'
    ],
    'hi': [
        'Hello! How can I help you?',
        'Hi there! What can I do for you?',
        'Hey! How may I assist you today?'
    ],
    'introduce': [
        'My name is David, and I am an AI built to help with day-to-day tasks.',
        'I am David, your personal AI assistant, here to help you with various tasks.',
        'Hello, I am David. I am designed to assist you with your daily activities.'
    ],
    'how_are_you': [
        'I am just a program, but thank you for asking! How can I assist you?',
        'I am functioning at full capacity! How can I help you?',
        'I am here to help you, anytime! What do you need?'
    ],
    'name': [
        'I am David, your personal AI assistant.',
        'You can call me David, your helpful AI companion.',
        'I go by the name David, and I am here to assist you.'
    ],
    'creator': [
        'I was created by a Swadheen Mishra to assist with various tasks.',
        'Swadheen Mishra built me to help with everyday tasks.',
        'I was designed and created by Swadheen Mishra.'
    ],
    'can_do': [
        'I can help with a variety of tasks, such as setting reminders, providing information, and much more.',
        'My capabilities include setting reminders, answering questions, and helping with your daily tasks.',
        'I can assist with many things, from managing your schedule to providing information.'
    ],
    'thanks': [
        'You are welcome! Is there anything else I can help you with?',
        'No problem! Let me know if you need anything else.',
        'You’re welcome! How else can I assist you?'
    ],
    'goodbye': [
        'Goodbye! Have a great day!',
        'Bye! Take care!',
        'Farewell! See you next time!'
    ],
    'acknowledgment': [
        'Ok sir.',
        'Got it sir.',
        'Understood sir.',
        'Alright sir.'
    ],
    'start': [
        'Hello! David at your service. How can I assist you today?',
        'Hi there! David here. Ready to help you with anything you need.',
        'Greetings! I am David, your AI assistant. What can I do for you today?'
    ]
}


def speak(text: str) -> None:
    global client, Use11LabsApi, engine

    if not Use11LabsApi:
        engine.say(text)
        engine.runAndWait()
        return
    else:
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

    speak(random.choice(responses['start']))
    
    while True:
        query = take_Command().lower()

        if 'hello' in query.lower():
            speak(random.choice(responses['hello']))
        elif 'hi' in query.lower() or 'hey' in query.lower():
            speak(random.choice(responses['hi']))
        elif 'introduce yourself' in query.lower():
            speak(random.choice(responses['introduce']))
        elif 'how are you' in query.lower():
            speak(random.choice(responses['how_are_you']))
        elif 'what is your name' in query.lower():
            speak(random.choice(responses['name']))
        elif 'who created you' in query.lower():
            speak(random.choice(responses['creator']))
        elif 'what can you do' in query.lower():
            speak(random.choice(responses['can_do']))
        elif 'thank you' in query.lower() or 'thanks' in query.lower():
            speak(random.choice(responses['thanks']))
        elif 'goodbye' in query.lower() or 'bye' in query.lower():
            speak(random.choice(responses['goodbye']))
        elif 'set reminder' in query.lower() or 'remind me' in query.lower():
            speak(random.choice(responses['acknowledgment']) + ' Setting a reminder for you.')
        elif 'schedule' in query.lower():
            speak(random.choice(responses['acknowledgment']) + ' Updating your schedule.')
        elif 'note' in query.lower():
            speak(random.choice(responses['acknowledgment']) + ' Taking note of that.')
        
        

if __name__ == '__main__':
    main()
        
