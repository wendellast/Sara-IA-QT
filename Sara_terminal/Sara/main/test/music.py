def play(arquivos):
    from playsound import playsound
    import multiprocessing
    
    m = multiprocessing.Process(target=playsound, args=(arquivos + '.mp3',))
    m.start()
    
    
    
    input('presione "enter para parar') 
    
    m.terminate()



    
    