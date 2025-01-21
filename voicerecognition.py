# Install SpeechRecognition with pip install speech_recognition
# Install pyaudio module using pip install pyaudio
# pip install setuptools
# pip install pyaudio
# pip install pyttsx3

import speech_recognition as sr
import webbrowser
import pyttsx3  

recognizer = sr.Recognizer()   
engine = pyttsx3.init()

def talk(): 
    mic = sr.Microphone()  
    with mic as source:

        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio, language='ES')

    print(f"Has dicho: {text}")
    return text.lower()   

if "amazon" in talk():

    engine.say("¿Qué producto buscas?")
    engine.runAndWait()
    text = talk()
    webbrowser.open(f"https://www.amazon.es/s?k={text}")
    
