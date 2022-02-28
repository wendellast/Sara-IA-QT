import pyttsx3

speak = pyttsx3.init('espeak')

while True:
    phrase = input('Enter a text: ')

    speak.say(phrase) 
    speak.runAndWait()