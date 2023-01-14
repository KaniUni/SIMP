import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

class WhatsApp:

    def speak(audio):

        engine.say(audio)
        engine.runAndWait()

    def takeCommand():
        var = WhatsApp
        r=sr.Recognizer()
        #print(sr.Microphone.list_microphone_names())
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            # r.energy_threshold()
            print("speak now : \n listening....")
            
            audio= r.listen(source)
            try:
                query = r.recognize_google(audio)
                print(query)
            except Exception as e:
                print("sorry, could not recognise. Say that again")
                return "None"


            return query


    def working_func():
        var=WhatsApp
        var.speak("say person's name you want to text")
        print("say person's name you want to text")
        query = var.takeCommand().lower()
        dict1= {'aman':'+917518125057','amit':'+919413081753', 'ansh':'+918868944498', 'adi': '+918962433150'}
        index = query.rindex(" ")
        name = query[(index+1)::]
        if name in dict1:
            num = dict1[name]
            
        else:
            var.speak("name not found in dictionary. please say number")
            print("name not found in dictionary. please say number")
            query2= var.takeCommand()
            num= "+91"+query2
            num = num.replace(" ", "")

            if len(num)==13:
                pass
            else:
                while(len(num)!=13):
                    var.speak("Sorry num not acceptable. Retry")
                    print("Sorry num not acceptable. Retry")
                    query_spc= var.takeCommand()
                    num= "+91"+query2
                    num = num.replace(" ", "")

        print("Please speak the message you want to send")
        var.speak("Please speak the message you want to send")
        query3= var.takeCommand().lower()
        a = int(datetime.datetime.now().strftime("%H "))
        b = int(datetime.datetime.now().strftime("%M "))
        pywhatkit.sendwhatmsg(num, query3 , a, (b+1), 8, True,2)




def main():
    variable = WhatsApp
    variable.working_func()
    # query = var.takeCommand().lower()
    # dict1= {'aman':'+917518125057','amit':'+919413081753', 'ansh':'+918868944498', 'adi': '+918962433150'}
    # index = query.rindex(" ")
    # name = query[(index+1)::]
    # if name in dict1:
    #     num = dict1[name]
        
    # else:
    #     var.speak("name not found in dictionary. please say number")
    #     print("name not found in dictionary. please say number")
    #     query2= var.takeCommand()
    #     num= "+91"+query2
    #     num = num.replace(" ", "")

    #     if len(num)==13:
    #         pass
    #     else:
    #         while(len(num)!=13):
    #             var.speak("Sorry num not acceptable. Retry")
    #             print("Sorry num not acceptable. Retry")
    #             query_spc= var.takeCommand()
    #             num= "+91"+query2
    #             num = num.replace(" ", "")

    # print("Please speak the message you want to send")
    # var.speak("Please speak the message you want to send")
    # query3= var.takeCommand().lower()
    # a = int(datetime.datetime.now().strftime("%H "))
    # b = int(datetime.datetime.now().strftime("%M "))
    # pywhatkit.sendwhatmsg(num, query3 , a, (b+1), 8, True,2)
if __name__=="__main__":
    main()