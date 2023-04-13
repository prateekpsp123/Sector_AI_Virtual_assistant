import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
name = "Prateek"
what_to_call = "sir"
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
        speak(f"Good Morning {name} {what_to_call}, Hope you are doing well, tell me what can i do for you ?")
    elif hour > 12 and hour < 18:
        speak(f"Good evening {name} {what_to_call}, Hope you are doing well, tell me what can i do for you ?")
    else:
        speak(f"Good evening {name} {what_to_call}, Hope you are doing well, tell me what can i do for you ?")       

def take_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.........")   
        query = r.recognize_google(audio, language='en-in') 
        print(f"user said: {query}")
    except Exception as e:
        print("Please say that again sir !")   
        return "None"
    return query 

if __name__ == "__main__":
    wishMe()
    while True:
        query = take_Command().lower()

        #Logic for executing the task 
        if "what" in query or "who" in query or "tell" in query or "which" in query: 
            speak("sure sir, searching about this")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("This is what i found !")
            speak(result)
