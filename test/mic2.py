import speech_recognition as sr

def reconhecimento_voz():
    # Inicializa o reconhecedor
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Diga algo:")
        # Ajusta o nível de ruído do ambiente
        recognizer.adjust_for_ambient_noise(source)
        
        # Escuta o áudio do microfone
        audio = recognizer.listen(source)
    
    try:
        # Reconhece o discurso usando o serviço do Google Speech Recognition
        texto_reconhecido = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse: " + texto_reconhecido)
        return texto_reconhecido
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return None
    except sr.RequestError as e:
        print("Erro ao requisitar resultados; {0}".format(e))
        return None

# Chama a função para iniciar o reconhecimento de voz e imprime o texto reconhecido
texto_falado = reconhecimento_voz()
if texto_falado is not None:
    print("Texto falado: " + texto_falado)
