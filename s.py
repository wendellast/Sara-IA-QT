import sys
import platform
import pyttsx3
import speech_recognition as sr

vozes = sr.Recognizer()
sara_voz=pyttsx3.init()


with sr.Microphone() as s:

    audio = vozes.listen(s)

#print(voz)
'''
with sr.Microphone() as s:
        audio = vozes.listen(s)
   
        speech2 = vozes.recognize_google(audio, language= "pt-BR")
        print(speech2)'''
