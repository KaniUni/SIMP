import speech_recognition as sr
import webbrowser, pyttsx3,os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    #print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        print("say anything : ")
        audio= r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(query)
        except:
            print("sorry, could not recognise. Say that again")
            return "none"

        return query

    
if __name__=="__main__" :
    query = takeCommand().lower()
    if 'play music' in query:
            speak("Do you want to play it from local directory or online in audio or video format")

            query2 = takeCommand().lower()
            if 'local' in query2:
                music_dir = 'G:\\beats_audio'  #write the address of file in which your music is stored
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))   #here we can also use the random function to generate a random index number and then play the song
            elif 'audio' in query2:
                webbrowser.open("spotify.com/query")
            elif 'video' in query2:
                webbrowser.open("https://www.youtube.com/results?search_query=kesariya")