#pip install pyttsx3
import pyttsx3 as p
import speech_recognition as sr
import randfacts
import datetime

from selenium_web1 import infow
from YT_vedio import MusicPlayer
from News import *
from jokes import *
from weather import *

#Converting speech to text - speech recognotion module
#install- pip install SpeechRecognitiom

#use anaconda to install py audio
#conda install PyAudio

engine =p.init() #it gets the information of current driver you are using
# we can change the voice or adjust 
rate=engine.getProperty('rate')
#print(rate) gives output 200
#we can set the rate
engine.setProperty('rate',130)
voices=engine.getProperty('voices')
#print(voices)
#prints list of thevoices which windows offer.. we run any one of it
#engine.setProperty('voices',voices[0].id) #gives male voice
engine.setProperty('voice',voices[1].id) 

def speak(text):
    engine.say(text)#Change the rate from 180 to 130 
    # say method tell the engine to wait adn run and Wait waits until say is finished
    engine.runAndWait()

today_date=datetime.datetime.now()

#function to wish
def wishme():
    hour=int(datetime.datetime.now().hour) #accesses hour of the date
    if hour>0 and hour<12:
        return("MORNING")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

r=sr.Recognizer() #instance is created to retrive audio from microphone

speak("hello sir, Good"+ wishme() +" I'm your voice assistant.")


#date and time ... import date module and use today_date 
#strftime converts date into readable string 
#we can go throgh w3school to know %d,%B
speak("Today is "+today_date.strftime("%d") + " of " + today_date.strftime("%B") + " And its currently " +today_date.strftime("%I %M %p"))

#weather 
#we make use of API s
#get API key from OpenWeatherAPI.org
#weather.py
speak("Temperature in Mangaluru is " +str(temp()) + "degree Celcius  and with " + str(des()))


speak(" How are you? ")

with sr.Microphone() as source:
    #energy_threshold it will increase the spectrum of voice
    r.energy_threshold=10000
    #capture all noices around
    r.adjust_for_ambient_noise(source,1.2)
    print("listenng")
    
    audio=r.listen(source)
    #Audio sent to google speech api to convert it to text
    text=r.recognize_google(audio)
    print(text)
    #It will capture what we say and sent to google speech 

if "what" and "about" and "you" in text:
    speak("I am having a good day sir")
speak("what can I do for you?")

#information from web display the related info
#automation: for that we use selenium web driver




#now we import infow function from selenium_web1.py and ask assiatant to get some information from wikipedia
#make assistant to speack few lines of the content searched by automation using selenium
with sr.Microphone() as source:
    #energy_threshold it will increase the spectrum of voice
    r.energy_threshold=10000
    #capture all noices around
    r.adjust_for_ambient_noise(source,1.2)
    print("listening....")
    audio = r.listen(source)
    text2= r.recognize_google(audio)

if "information" in text2:
    speak ("you need information related to which topic?")
    with sr.Microphone() as source:
        #energy_threshold it will increase the spectrum of voice
        r.energy_threshold=10000
        #capture all noices around
        r.adjust_for_ambient_noise(source,1.2)
        print("listening....")
        audio = r.listen(source)
        infor= r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))

#call function from selenium_web1.py to get information from wikipedia
    assist = infow()
    assist.get_info(infor)




#similarly get youtube vedios and all
# for that code is in YT_vedio.py

elif "play" in text2 and "video" in text2:
    speak("you want to play which vedio??")
    with sr.Microphone() as source:
        #energy_threshold it will increase the spectrum of voice
        r.energy_threshold=10000
        #capture all noices around
        r.adjust_for_ambient_noise(source,1.2)
        print("listening....")
        audio = r.listen(source)
        vid= r.recognize_google(audio)
    speak("playing {} on youtube".format(vid))
    assist=MusicPlayer()
    assist.play(vid)



#now giving latest news  we use API
#News.py
#we use API
#get API from newsAPI.org
#save in .env file and do't forget to add it to .gitignore for security
elif "news" in text2:
    print("Sure sir Now I will read news for you")
    speak("Sure sir Now I will read news for you")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

#now we make program to say random and intersting facts for us
# we do not use of any API , instead we have a module randfacts
#pip install randfacts
elif "fact" in text2:
    speak("Sure sir,")
    x=randfacts.get_fact()
    print(x)
    speak("Did you know that, "+x)

#jokes.py
#ask assistant to tell jokes
elif "joke" or "jokes" in text2:
    speak("Sure sir , get ready for some chuckles")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])




        



