import speech_recognition as sr
import os
from sys import platform
import asyncio
#global vars
r = sr.Recognizer()
mic = sr.Microphone()


def clear():
    if platform.startswith('linux'):
        os.system('clear')
    elif platform.startswith('win'):
        os.system('cls')


async def commands(text):
    print(text)
    if text == "abrir editor":
         os.system('code-insiders')
    elif text == "abrir navegador":
         os.system('brave-browser')
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


async def main():
    _break = False
    clear()
    while not _break:
        text = listen()
        _break = await commands(text)

if __name__ == "__main__":
    asyncio.run(main())