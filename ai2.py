import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyjokes
from datetime import date
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def t2s(text):
    obj.text2speech(text)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Please tell me how may I help you")       

def takeCommand():
    

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
           
        print("Say that again please...")  
        return "None"
    query = query.lower()    
    return query

   

           

def TaskExecution():
    wishMe()
    while True:
        query = takeCommand()
           
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results) 

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")          

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
    
        elif 'open code' in query:
            codePath = "C:\\Users\\Ayush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'joke' in query:
          tell_joke = pyjokes.get_joke(language="en", category="all")
          print(tell_joke)
          speak(tell_joke)

        elif 'date' in query:
            today = date.today()
            dt = today.strftime("%B %d, %Y")
            print(dt)
            speak(f"sir the date is {dt}")

        elif ' news' in query:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()    

            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")

            speak("here are the latest news for you")            
            for news in news_list:
             print(news.title.text)
             print(news.pubDate.text)
             print("-"*60)

       
        elif "temperature" in query:
            speak("In which City Sir?")
            city = takeCommand().lower()
            search = f"temperature in {city} "
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = soup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f"current temprature in {city} is {temp}") 
            speak(f"Current {search} is {temp}")
                
            
        elif"hello" in query:
            speak("hello, may i help you with something")

        elif"how are you" in query:
            speak("i am fine, what about you?")

        elif"thank you" in query:
            speak("its my pleasure sir")


        elif "you can sleep" in query or "sleep now " in query:
            speak("okay sir , going to sleep, call me anytime")
            break
          

if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "wake up" in permission:
            TaskExecution()
        elif "stop" in  permission:
            speak("thanks for using me")
            sys.exit()
            