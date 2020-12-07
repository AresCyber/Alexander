import speech_recognition as sr
import pyttsx3 
from time import sleep
def voicepass(password): 
    fcount = 0
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    r = sr.Recognizer()
    speech = sr.Microphone(device_index=1)


    while fcount != 6:
        try:
            with speech as source:
                audio = r.record(source, duration=4)
            recog = r.recognize_google(audio, language = 'en-US')
            if recog == password: 
                engine.say("Access Granted")
                access = 1
                #print(recog)
                engine.runAndWait()
                return access
            else:
                #get fcount
                fcount += 1
                engine.say("Voice not recognized, please try again, you have " + str(6 - fcount) + "Tries left")
                engine.runAndWait()
                if fcount == 6: 
                    return 0
           
        except sr.UnknownValueError:
           engine.say("Google Speech Recognition could not understand audio")
           engine.runAndWait()
        except sr.RequestError as e:
           engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
           engine.runAndWait()

def playsound(soundbyte):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    try: 
        engine.say(str(soundbyte))
        engine.runAndWait()
    except: 
        return

def backdoor(backdoorpass):
    fcount = 0
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    r = sr.Recognizer()
    speech = sr.Microphone()

    while fcount != 6:
        try:
            print("starting record")
            with speech as source:
                #r.adjust_for_ambient_noise(source)
                audio = r.record(source, duration=4)
            print("Recorded audio")
            recog = r.recognize_google(audio, language = 'en-US')
            print(recog)
            if recog == backdoorpass:
                engine.say("password accepted")
                engine.runAndWait()            

            else:
                fcount += 1
                engine.say("Voice not recognized, please try again, you have " + str(6 - fcount) + "Tries left")
                engine.runAndWait()
                if fcount == 6: 
                    return 0

        except sr.UnknownValueError:
            engine.say("couldn't understand audio back try again")
            engine.runAndWait()
            sleep(1)
        except sr.RequestError as e:
            engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
            engine.runAndWait()
            sleep(1)
            #ideally a backup or offline tts module would be placed here
            return 0