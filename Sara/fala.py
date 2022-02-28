import pyttsx3

speak = pyttsx3.init('dummy')

while True:
    phrase = input('Enter a text: ')

    speak.say(phrase) 
    speak.runAndWait()