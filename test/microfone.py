
from vosk import Model, KaldiRecognizer
import pyaudio

model = Model("model-br")
rec = KaldiRecognizer(model, 16000)

# Preparando o microfone para captura
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def mc():
    while True:
        rec.pause_threshold = 1
        # Lendo audio do microfone
        data = stream.read(20000)
        # Convertendo audio em texto
        rec.AcceptWaveform(data)  
        

        try:
            Input = rec.Result()
            print(Input)
        except:
            # Retorna os erros
            print('Não entendi, fale novamente ! ')
            #resposta("Não entendi o que você disse, fale novamente.")
            return 'none'
        #Input = Input.lower()
    return Input

mc()
