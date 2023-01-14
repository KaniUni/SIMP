import pyttsx3, datetime, wikipedia, webbrowser,os, smtplib, random,requests, bs4
import speech_recognition as sr
import HandTrackingmodule as htm
import pywhatkit
from VolumeGuesture import volumeguesture
from WhatsApp import WhatsApp
from HandGame import HandGame
from RockPaperScissors import RockPaperScissors
from ZOOMINOUT import ZOOMINOUT
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am SIMP sir! How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aiman_k@bt.iitr.ac.in', '22124004') #your email and password here 
    server.sendmail('aiman_k@bt.iitr.ac.in', to, content) # your email here
    server.close()

        
def takeCommand():
    r=sr.Recognizer()
    #print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        print("say anything : \n listening....")
        audio= r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(query)
        except Exception as e:
            print("sorry, could not recognise. Say that again")
            return "None"

        return query






if __name__=="__main__" :
     wishMe()
     while 1:
        query = takeCommand().lower()

        # logic for query
        if 'wikipedia' in query:
            speak("searching in wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube...")

        elif 'open google' in query:
            webbrowser.open("google.com") 
            speak("Opening Google...")


        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening Stackoverfkow...")

        elif 'open netflix' in query:
            
            webbrowser.open("netflix.com")
            speak("Opening Netflix...")
        
        elif 'play music' in query:
            speak("Do you want to play it from local directory or online in audio or video format")

            query2 = takeCommand().lower()
            if 'local' in query2:
                music_dir = 'G:\\beats_audio'  #write the address of file in which your music is stored
                songs = os.listdir(music_dir)
                y = random.randrange(0,5)
                os.startfile(os.path.join(music_dir,songs[y]))   #here we can also use the random function to generate a random index number and then play the song
            elif 'audio' in query2:
                search_keyword=query2.replace("in audio", "")
                webbrowser.open("https://open.spotify.com/search/"+search_keyword)
            elif 'video' in query2:
                search_keyword=query2.replace("in video", "")
                #webbrowser.open("https://www.youtube.com/results?search_query="+search_keyword)
                pywhatkit.playonyt(search_keyword)
                

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H : %M :%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\KANIKA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening visual studio code...")
        
        elif 'weather' in query:
            index = query.rindex(" ")
            city = query[index::]
            print(city)
            url = "https://google.com/search?q=weather+in+" + city
            request_result = requests.get( url )
            soup = bs4.BeautifulSoup( request_result.text , "html.parser" )
            temp = soup.find( "div" , class_='BNeawe' ).text 
            print(temp) 
            speak("Current temperature in")
            speak(city)
            speak("is")
            speak(temp)


        elif 'whatsapp' in query:
            WhatsApp.working_func()




        elif 'email kanika' in query:
            try:
                speak("whats the content of mail?")
                content = takeCommand()
                to = 'kanikauni24@gmail.com'
                sendEmail(to, content)
                speak("email has been sent")
            
            except Exception as e:
                print(e)
                speak("Sorry! Email has'nt been sent.")
        
        elif 'enable volume control' in query:
            print("ENABLED HAND CONTROLLED VOLUME GUESTURE")
            speak("ENABLED HAND CONTROLLED VOLUME GUESTURE")
            volumeguesture.callvg()

        elif 'play game' in query:
            print("Game is starting...")
            speak("Game is starting...")
            HandGame.HandGame()
        elif 'rock paper scissors' in query:
            print("Game is starting...")
            speak("Game is starting...")
            RockPaperScissors.play_func()
        elif "zoom" in query:
            print("Enabling zoom ....")
            speak("Enabling zoom ....")
            ZOOMINOUT.ZOOMINOUT()


        elif 'quit now' in query:
            print("Thank you for using my service")
            speak("Terminating the program. Thank you for using our service")
            break
        else:
            continue



