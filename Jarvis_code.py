import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning Prateek sir")
    elif hour > 12 and hour < 18:
        speak("Good evening Prateek sir")
    else:
        speak("Good evening Prateek sir")       

if __name__ == "__main__":
    wishMe()
    speak("Hope you are doing well, tell me what can i do for you ?")    
    