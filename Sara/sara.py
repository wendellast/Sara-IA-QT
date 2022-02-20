#Sara IA 
import speech_recognition as sr
import pyttsx3
import datetime


#Reconhesedor
audio = sr.Recognizer()
maquina = pyttsx3.init()



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
        
        
usuario()
        
    