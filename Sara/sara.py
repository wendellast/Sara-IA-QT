#Sara IA 
import speech_recognition as sr
import pyttsx3
import datetime

#Reconhesedor
audio = sr.Recognizer()
<<<<<<< HEAD
maquina = pyttsx3.init('espeak')
maquina.say('olá, eu sou a sara')
maquina.say('como posso ajudar')
maquina.runAndWait()

=======
maquina = pyttsx3.init()
maquina.say('ola sou tina')
maquina.runAndWait()
>>>>>>> 6e1586d307ceb3e6d95b1025c0bb46c957cbb991


def executar():
    
    #Micophone
    try:
        with sr.Micophone() as source:
            print('Ouvindo... ')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz,  language='pt-BR')
            comando = comando.lower()
            
            #Sara fala
            if  'sara' in comando:
                comando = comando.replace('sara', '')
                maquina.say(comando)
                maquina.runAndWait()

            
    except:
        print('Mricofone não está fucionando')    

    return comando

#Usuario
def usuario():
    comando = executar()
    
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
        
        

        
    