import pyttsx3
from flask import Flask, request
from rich import print
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os

#Reconhecedor de Audio
audio = sr.Recognizer()
speak = pyttsx3.init('sapi5-Letícia-F123')



        
        
def test_fala():
    speak = pyttsx3.init()

    while True:
        phrase = input('Enter a text:    ')

        speak.say(phrase) 
        speak.runAndWait()

test_fala()