import speech_recognition as sr
import pyttsx3
import os
import datetime
import requests
from translate import Translator

#from kivy.lang import Builder
#from kivy.uix.screenmanager import Screen, ScreenManager
#from kivy.uix.label import Label
#from kivy.uix.button import Button
#from kivy.uix.widget import Widget
#from kivy.uix.image import Image
#from kivymd.uix.label import MDLabel
#from kivymd.app import MDApp
#from kivymd.uix.button import MDRaisedButton
#from kivymd.uix.button import MDRoundFlatIconButton


def tradutor(palavra):
    translator= Translator(to_lang="pt")
    translation =  translator.translate(palavra)
    return translation


def convertFala(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()



def ouvir():

    rec = sr.Recognizer()


    with sr.Microphone() as mic:
        print("ouvindo")
        rec.adjust_for_ambient_noise(mic)
        audio = rec.listen(mic)

    try:
        texto = rec.recognize_google(audio, language="pt-BR")

        if "lista de frases" in texto:
            convertFala("Essas são as frases que você pode falar para mim")
            print("1- Previsão do tempo ")
            print("2- Conhecer um local novo")
            print("3- Lista de Desejos")
            print("4- Viajar")
            print("5- Locais mais visitados em cada estação")
            print("6- Roteiro de Viagem")

        elif "viajar" in texto:
            convertFala("Olá, bem-vindo a sua Assistente Virtual de Viagens")
            convertFala("Me chamo Mó Viagem hihihi, no que posso te ajudar?")


        elif "previsão do tempo" in texto:
            convertFala("Para onde você pretende ir")
            api = "a143cba82f2ee6901732e51ece9014df"
            cidade = str(input("Qual o nome da cidade?"))
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api}"
            req = requests.get(url)
            requisicao_dic = req.json()
            tempo = requisicao_dic['weather'][0]['description']
            temperatura = requisicao_dic['main']['temp']
            converter = (temperatura - 273.15) // 1
            clima = tradutor(tempo)
            convertFala(f"Em {cidade} faz agora {converter} graus Celsius")
            convertFala(f"A condição climática é {clima}")
            print(f"Temperatura agora em {cidade} é {converter} °C")
            print(f"Condição climática agora em {cidade} é {clima}")

            if (converter >= 28):
                convertFala("Passe um filtro solar e beba bastante água, hoje será um dia quente")

            elif (converter <= 15):
                convertFala("Melhor se agasalhar, hoje o dia vai estar frio")

            elif (converter >= 16 and converter <= 27):
                convertFala("Hoje o clima estará agradável, aproveite")


        elif "até mais" in texto:
            convertFala("Até uma outra ocasião, beijos beijos")
            print("Estarei esperando o seu retorno :)")
            breakpoint()

         #elif "curiosidades sobre uma cidade" in texto:



    except sr.UnknownValueError:
        convertFala("Não entendi, poderia repetir")

    return texto



#class Tela(MDApp):

#    def build(self):
#        self.theme_cls.theme_style = "Light"
#        self.theme_cls.primary_palette = "Teal"
#       self.title = "Assistente Virtual - Mó Viagem"
#        return Builder.load_file('tela.kv')



while True:
    #Tela().run()
    ouvir()