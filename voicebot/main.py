import speech_recognition as sr
import pyttsx3 
import wikipedia
import pywhatkit
listener=sr.Recognizer()
player=pyttsx3.init()
def listen():
    with sr.Microphone() as input_device:
        print("Im listening .... speak")
        voicecontent=listener.listen(input_device)
        text_cmd=listener.recognize_google(voicecontent)
        return text_cmd.lower()

def speak(text):
    player.say(text)
    player.runAndWait()
    
      
def runbot():
    textcmd=listen()
    # if "hello" or "hi" or "alexa" in textcmd:
    #     speak("hello nice to meet you! this is alexa")
    if "alexa" in textcmd:
        if "what is" in textcmd:
            textcmd=textcmd.replace("alexa","")
            textcmd.replace ("what is","")
            infotext=wikipedia.summary(textcmd,5)
            speak(infotext)
        elif "who is" in textcmd:
            textcmd.replace ("who is","")
            infotext=wikipedia.summary(textcmd,5)
            speak(infotext)
        elif "when is" in textcmd:
            textcmd.replace ("when is","")
            infotext=wikipedia.summary(textcmd,5)
            speak(infotext)
        elif "play" in textcmd:
            textcmd.replace ("play","")
            pywhatkit.playonyt(textcmd)
        else:
            speak("unable to find what you are looking for")
runbot()


