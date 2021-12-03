from multiprocessing.sharedctypes import Value
from time import sleep
from sys import platform
from click import command
import speech_recognition as sr
import json
import os

def clear():
    if platform.startswith('linux'):
        os.system('clear')
    elif platform.startswith('win'):
        os.system('cls')


def dump_json(commands):
    with open('commands.json', 'w') as json_file:
            json.dump(commands, json_file)


def load_json():
    try:
        with open('commands.json', 'r') as json_file:
            _commands = json.load(json_file)
        return _commands
    except:
        _commands = {}
        for key in preload:
            _commands[key] = key
        dump_json(_commands)
        return _commands


def insert_cmd():
    key = input('Qual a chave que quer usar para acionar o comando? (Use underline ao inves de espaço e coloque tudo em minuscula)\n-> ')
    if key in ("comando", "encerrar"):
        print('Isso não é possivel')
        return
    cmd = input('Qual comando quer colocar?\n-> ')
    commands[key] = cmd
    dump_json(commands)


def delete_cmd():
    key = input("Qual comando deseja remover²\n-> ")
    if key in preload:
        print('Não é possivel!')
        return
    
    try:
        commands.pop(key)
        dump_json(commands)
    except:
        print("Não foi possivel")


def to_list():
    print('\n'.join(str(f'{key}: {value}') for key, value in commands.items()))
    input('Tecle qualquer tecla para continuar')

def commands_central(key):
    print(key)
    if key in commands and key not in preload:
        try:
            os.system(commands[key])
        except Exception as error:
            print(f'Não foi possivel executar esse comando por causa de:\n{error}')
    elif key == "adicionar":
        insert_cmd()
    elif key == "encerrar":
        return True
    elif key == "remover":
        delete_cmd()
    elif key == "listar":
        to_list()
    else:
        print('Nenhum comando com esse nome!')

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
            return text.replace(' ', '_').lower()
    except:
        return 'Não entendi!'


def main():
    _break = False
    clear()
    while not _break:
        text = listen()
        _break = commands_central(text)
        

if __name__ == "__main__":
    #global vars
    preload = ("adicionar", "encerrar", "remover", "listar")
    r = sr.Recognizer()
    mic = sr.Microphone()
    commands = load_json()
    main()
    