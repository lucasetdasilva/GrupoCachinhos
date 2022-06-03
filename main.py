import speech_recognition as sr
import pyttsx3
import requests
import pandas as pd
import wikipedia
from translate import Translator
import re
import holidays
feriados = holidays.Brazil()
Av={}

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

        if "viajar" in texto:
            convertFala("Olá, bem-vindo a sua Assistente Virtual de Viagens")
            convertFala("Me chamo Mó Viagem hihihi, no que posso te ajudar?")

        #Previsão do tempo
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

        #Locais mais vistado em cada estação
        elif "locais mais visitados" in texto:
            outono = ["Pantanal", "Chapada dos Veadeiros", "Gramado", "Campos do Jordão", "Florianópolis"]
            inverno = ["Diamantina", "Monte Verde", "São bento do Sapucaí", "Bento Gonçalves", "Vale dos Vinhedos"]
            primavera = ["Atibaia", "Holambra", "Cunha", "Poços de Caldas", "Belo Horizonte"]
            verao = ["Fortaleza", "Aracajú", "Recife", "Caldas Novas", "Porto Seguro"]
            convertFala('Por Favor diga uma estação:')
            estacao = ouvir()
            if "outono" in estacao:
                convertFala('os melhores locais para se viajar no outono:')
                print(outono)
                convertFala(outono)
                
            elif "inverno" in estacao:
                convertFala('melhores destinos para curtir o frio do inverno:')
                print(inverno)
                convertFala(inverno)
                
            elif "primavera" in estacao:
                convertFala('onde aproveitar a estação das flores:')
                print(primavera)
                convertFala(primavera)
                
            elif "verão" in estacao:
                convertFala('Cidades para aproveitar o calor do verão:')
                print(verao)
                convertFala(verao)

        #Calendario de Feriados
        elif "calendario" or "calendario de feriados" in texto:
          convertFala("Digite o mes que deseja saber os feriados ")
          mf = sr.Recognizer()

          if mf=='janeiro':
              for feriado in feriados['2020-01-01': '2020-01-31'] :
                convertFala('As datas com feriado em Janeiro são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)


          elif mf=='fevereiro':
              for feriado in feriados['2020-02-01': '2020-02-28'] :
                convertFala('As datas com feriado em Fevereiro são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='março':
              for feriado in feriados['2020-03-01': '2020-03-31'] :
                convertFala('As datas com feriado em Março são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='abril':
              for feriado in feriados['2020-04-01': '2020-04-30'] :
                convertFala('As datas com feriado em Abril são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='maio':
              for feriado in feriados['2020-05-01': '2020-05-30'] :
                convertFala('As datas com feriado em Maio são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='junho':
              for feriado in feriados['2020-06-01': '2020-06-31'] :
                convertFala('As datas com feriado em Junho são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='julho':
              for feriado in feriados['2020-07-01': '2020-07-30'] :
                convertFala('As datas com feriado em Julho são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='agosto':
              for feriado in feriados['2020-08-01': '2020-08-31'] :
                convertFala('As datas com feriado em Agosto são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='setembro':
              for feriado in feriados['2020-09-01': '2020-09-30'] :
                convertFala('As datas com feriado em Setembro são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='outubro':
              for feriado in feriados['2020-10-01': '2020-10-31'] :
                convertFala('As datas com feriado em Outubro são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='novembro':
              for feriado in feriados['2020-11-01': '2020-11-30'] :
                convertFala('As datas com feriado em Novembro são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

          elif mf=='dezembro':
              for feriado in feriados['2020-12-01': '2020-12-31'] :
                convertFala('As datas com feriado em Dezembro são: \n')

                x=str(feriados)
                x=re.sub("datetime.date",'',x)
                x=re.sub('{','',x)
                x=re.sub('}','',x)

                print(x)

        #pesquisar agencias
        elif "pesquisar agências" in texto:
            convertFala("Qual tipo de viagem você prefere")
            print("1- Ecoturismo")
            print("2- Para toda família")
            print("3- Gastronômico")
            print("4- Parques temáticos")

            col_names =['gastronomico', 'descricaog', 'urlg', 'aventura', 'descricaoa', 'urla', 'familia', 'descricaof', 'urlf', 'parque', 'descricaop', 'urlp']
            tabela = pd.read_excel('api.xlsx', names = col_names)

            rec = sr.Recognizer()

            with sr.Microphone() as mic:
                print("Escolha um para prosseguir")
                rec.adjust_for_ambient_noise(mic)
                audio = rec.listen(mic)
            opcao = rec.recognize_google(audio, language="pt-BR")

            if "ecoturismo" in opcao:
                convertFala("Essas são as opções de viagens de Ecoturismo")
                eco = tabela['aventura'][:]
                print(eco)
                print("\n")
                convertFala("Caso tenha se interessado em alguma agência, clique no link para ser redirecionado para o site")
                eco2 = tabela['urla'][:]
                print(eco2)

                convertFala("Quer ver a descrição das agências")

                rec = sr.Recognizer()

                with sr.Microphone() as mic:
                    print("Escolha um para prosseguir")
                    rec.adjust_for_ambient_noise(mic)
                    audio = rec.listen(mic)
                escolha = rec.recognize_google(audio, language="pt-BR")

                if "sim" in escolha:
                    convertFala("Aqui está")
                    desc = tabela['descricaoa']
                    print(desc)

                elif "não" in escolha:
                    convertFala("Tudo bem")

                else:
                    convertFala("Não entendi")

            elif "para toda família" in opcao:
                convertFala("Essas são as opções de viagens para toda família")
                famil = tabela['familia'][:]
                print(famil)
                print("\n")
                convertFala("Caso tenha se interessado em alguma agência, clique no link para ser redirecionado para o site")
                famil2 = tabela['urlf'][:]
                print(famil2)

                convertFala("Quer ver a descrição das agências")

                rec = sr.Recognizer()

                with sr.Microphone() as mic:
                    print("Escolha um para prosseguir")
                    rec.adjust_for_ambient_noise(mic)
                    audio = rec.listen(mic)
                escolha2 = rec.recognize_google(audio, language="pt-BR")

                if "sim" in escolha2:
                    convertFala("Aqui está")
                    desc2 = tabela['descricaof']
                    print(desc2)

                elif "não" in escolha2:
                    convertFala("Tudo bem")

                else:
                    convertFala("Não entendi")

            elif "gastronômico" in opcao:
                convertFala("Essas são as opções de viagens gastronômicas")
                gastronomia = tabela['gastronomico'][:]
                print(gastronomia)
                print("\n")
                convertFala("Caso tenha se interessado em alguma agência, clique no link para ser redirecionado para o site")
                gastronomia2 = tabela['urlg'][:]
                print(gastronomia2)

                convertFala("Quer ver a descrição das agências")

                rec = sr.Recognizer()

                with sr.Microphone() as mic:
                    print("Escolha um para prosseguir")
                    rec.adjust_for_ambient_noise(mic)
                    audio = rec.listen(mic)
                escolha3 = rec.recognize_google(audio, language="pt-BR")

                if "sim" in escolha3:
                    convertFala("Aqui está")
                    desc3 = tabela['descricaog'][:]
                    print(desc3)

                elif "não" in escolha3:
                    convertFala("Tudo bem")

                else:
                    convertFala("Não entendi")

            elif "parques temáticos" in opcao:
                convertFala("Essas são as opções de viagens de parques temáticos")
                par = tabela['parque'][:]
                print(par)
                print("\n")
                convertFala("Caso tenha se interessado em alguma agência, clique no link para ser redirecionado para o site")
                par2 = tabela['urlp'][:]
                print(par2)
                convertFala("Quer ver a descrição das agências")

                rec = sr.Recognizer()

                with sr.Microphone() as mic:
                    print("Escolha um para prosseguir")
                    rec.adjust_for_ambient_noise(mic)
                    audio = rec.listen(mic)
                escolha4 = rec.recognize_google(audio, language="pt-BR")

                if "sim" in escolha4:
                    convertFala("Aqui está")
                    desc4 = tabela['descricaop'][:]
                    print(desc4)

                elif "não" in escolha4:
                    convertFala("Tudo bem")

                else:
                    convertFala("Não entendi")

            else:
                convertFala("Esse parâmetro não existe")

        #despedida
        elif "até mais" in texto:
            convertFala("Até uma outra ocasião, beijos beijos")
            print("Estarei esperando o seu retorno :)")
            breakpoint()

        #elif "curiosidades sobre uma cidade" in text:
        
        #roteiro de viagens
        elif "roteiro" in texto:
            convertFala("Qual cidade você quer conhecer")

            rec = sr.Recognizer()

            with sr.Microphone() as mic:
                print("Por favor, fale o nome da cidade para saber o roteiro de viagem: ")
                rec.adjust_for_ambient_noise(mic)
                audio = rec.listen(mic)

            roteiro = rec.recognize_google(audio, language="pt-BR")

            wikipedia.set_lang('pt')

            resposta = wikipedia.page(roteiro)
            print('Roteiro da cidade escolhida: ', roteiro)
            print('\n')
            print("Caso retorne em branco não foi encontrado o roteiro da cidade desejada.")

            conteudo = resposta.section(section_title='Turismo')
            conteudo2 = resposta.section(section_title='Cultura')

            print(conteudo)
            convertFala(conteudo)

            print("Cultura da cidade:", roteiro)
            print('\n')
            print(conteudo2)
            convertFala(conteudo2)
            # A biblioteca wikipedia RETORNA NONE para subtópicos, ainda que correspondam ao tópico 'Turismo/Cultura' (função elif/else não funciona neste caso)
            print('')
            
            
        #Curiosidades
        elif "curiosidades" or "curiosidade" in texto:
            
            convertFala("Quer conhecer qual cidade")
            rec = sr.Recognizer()

            with sr.Microphone() as mic:
                print("Por favor, fale o nome da cidade para saber as curiosidades: ")
                rec.adjust_for_ambient_noise(mic)
                audio = rec.listen(mic)

            curiosidade = rec.recognize_google(audio, language="pt-BR")
                      
            wikipedia.set_lang('pt')
            
            resposta = wikipedia.summary(curiosidade, sentences=2)
            print(resposta)
            convertFala(resposta)
            
        elif "avaliações" in texto:
            convertFala("O que deseja fazer Ver Avaliações ou Fazer uma: ")
            Oqd = sr.Recognizer()
            
            if Oqd=="fazer avaliação":
 
                convertFala("Qual o local que deseja avaliar: "))
                s = sr.Recognizer()
                sa=str(input("Digite a sua avaliação e logo em seguida seu nome se desejar: "))

                if s in Av:
                    Av[s]+=(' , ')
                    Av[s]+=(sa)
                    s=''
                    sa=''
                else:
                    Av={**Av,**{s:sa}}
                    s=''
                    sa=''
            else:
                convertFala("De qual local deseja ver as avaliações: ")
                s = sr.Recognizer
                print(Av[s])
                s=''
         

    except sr.UnknownValueError:
        convertFala("Não entendi, poderia repetir")

    return texto

while True:
    ouvir()
