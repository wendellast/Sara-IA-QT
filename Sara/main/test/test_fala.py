import pyttsx3

def test_fala():
    speak = pyttsx3.init()

    while True:
        phrase = input('Enter a text:    ')

        speak.say(phrase) 
        speak.runAndWait()

test_fala()