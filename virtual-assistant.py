from time import sleep
from sys import platform
import speech_recognition as sr
import os

#global vars
r = sr.Recognizer()
mic = sr.Microphone()


def clear():
    if platform.startswith('linux'):
        os.system('clear')
    elif platform.startswith('win'):
        os.system('cls')

 
def commands(text):
    print(text)
    if text == "abrir vs code":
        os.system('code-insiders')
    elif text == "abrir navegador":
        os.system('brave-browser --disable-gpu --disable-software-rasterizer')
    elif text.startswith('encerrar'):
        return True
    
    return False


def listen():
    try:
        with mic as source:
            clear()
            print('Escutando...')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio, language = 'pt-BR')
            print('Analisando comando!')
            return text.lower()
    except:
        return 'Não entendi!'


def main():
    _break = False
    clear()
    while not _break:
        text = listen()
        _break = commands(text)
        sleep(2)
        

if __name__ == "__main__":
    main()
    