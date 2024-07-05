import pywhatkit
import pyttsx3  # Python text-to-speech library
import speech_recognition as sr  # Speech recognition library
import datetime  # Importa o dia e a hora
import requests
import random
import tkinter as tk
from PIL import Image, ImageTk


# CLIMA TEMPO
api_key = "ec618396f709f095eca5b37c605b2128"
location = "Indaiatuba"  # Replace with the location you want to get the forecast for
clima = ''

url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    forecast = data["list"][0]["weather"][0]["description"]
    if forecast == "clear sky":
        clima = "com o céu limpo"
    elif forecast == "few clouds":
        clima = "com poucas nuvens"
    elif forecast == "scattered clouds":
        clima = "nubládo"
    elif forecast == "broken clouds":
        clima = "com nuvens chuvosas"
    elif forecast == "shower rain":
        clima = "com chuvisco"
    elif forecast == "rain":
        clima = "com chuva"
    elif forecast == "thunderstorm":
        clima = "numa tempestade"
    elif forecast == "snow":
        clima = "nevando"
    elif forecast == "mist":
        clima = "com neblina"
    elif forecast == "light rain":
        clima = "com chuva leve"
    elif forecast == "moderate rain":
        clima = "com chuva moderada"
    elif forecast == "heavily intense rain":
        clima = "com chuva pesada intensa"
    elif forecast == "very heavy rain":
        clima = "com chuva muito pesada"
    elif forecast == "extreme rain":
        clima = "com chuva extremamente pesada"
    elif forecast == "freezing rain":
        clima = "com chuva congelante"
    elif forecast == "heavily intense rain":
        clima = "com chuva pesada intensa"
    elif forecast == "light intensity shower rain":
        clima = "com chuva chuvisco leve"
    elif forecast == "light intensity shower rain":
        clima = "com chuva chuvisco leve"

c1 = clima

now = datetime.datetime.now()  # Now = present time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize Tkinter window
window = tk.Tk()
window.title("J.A.R.V.I.S")

# Load GIF image
gif_image = Image.open("INICIO-VOCAL.gif")
gif_photo = ImageTk.PhotoImage(gif_image)

# Create a Label to display the GIF
gif_label = tk.Label(window, image=gif_photo)

# Define a function to update the GIF label
def update_gif_label(image_path):
    new_image = Image.open(image_path)
    new_photo = ImageTk.PhotoImage(new_image)
    gif_label.configure(image=new_photo)
    gif_label.image = new_photo

# Pack the GIF label into the window
#gif_label.pack()

# Resto do código...


# Define a function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()
    update_gif_label("ondas-de-audio.gif")  # Atualiza o GIF para exibir a fala


# Define a function to listen to user's voice command
def listen():
    with sr.Microphone() as source:
        speak("Como posso te ajudar?")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='pt-BR')
        print(f"You said: {text}")
        return text
    except:
        speak("Desculpe, não entendi.")
        return ""

# Resto do código...

# Main program loop
while True:
    command = listen()
    if "olá" in command.lower():
        speak("Olá mestre, como você está?")
        update_gif_label("ondas-de-audio.gif")  # Atualiza o GIF para exibir a resposta
    elif "estou bem e você" in command.lower():
        speak("Mestre, eu não sou vivo esqueceu?")
        update_gif_label("ondas-de-audio.gif")
    elif "bem e você" in command.lower():
        speak("Mestre, eu não sou vivo esqueceu?")
        update_gif_label("ondas-de-audio.gif")
    elif "qual o seu nome" in command.lower():
        speak("Meu nome é Jarvas!")
        update_gif_label("ondas-de-audio.gif")
    elif "horas" in command.lower():
        speak((now.strftime("São %H:%M")))
        update_gif_label("ondas-de-audio.gif")
    elif "qual o horário" in command.lower():
        speak((now.strftime("São %H:%M")))
    elif "que horas são" in command.lower():
        speak((now.strftime("São exatamente %H:%M:%S")))
    elif "qual o clima" in command.lower():
            speak(f"A previsão do tempo em {location} indica que está {c1}")
    elif "tocar música" in command.lower():
        if True:
            with sr.Microphone() as source:
                    speak("Qual Musica?")
                    audio = r.listen(source)
                    text = r.recognize_google(audio, language='pt-BR')
                    speak(f"Abrirei no YouTube a música {text}, para você!")
                    query = text
                    pywhatkit.playonyt(query)
    elif "música" in command.lower():
        if True:
            with sr.Microphone() as source:
                    speak("Qual Musica?")
                    audio = r.listen(source)
                    text = r.recognize_google(audio, language="en-US")
                    speak(f"Abrirei no YouTube a música {text}, para você!")
                    query = text
                    pywhatkit.playonyt(query)
    elif "adeus" in command.lower():
        speak("Até mais mestre.")
        break
    elif "até mais" in command.lower():
        speak("Até mais mestre.")
        break
    elif "tchau" in command.lower():
        speak("Até mais mestre.")
        break
    elif "conte-me uma piada" in command.lower():
        my_list = ["Qual é o cantor preferido dos castôres?                O Luiz Represas",
                "Como se sabe que o Estado é católico?                  porque tudo que se faz leva um terço",
                "Se estiver triste abraça com um sapato.                  Um sapato com sola", ]
        random_item = random.choice(my_list)
        speak(random_item)
    elif "uma piada" in command.lower():
        my_list = ["Qual é o cantor preferido dos castôres?                O Luiz Represas",
                    "Como se sabe que o Estado é católico?                  porque tudo que se faz leva um terço",
                    "Se estiver triste abraça um sapato.                  Um sapato com sola", ]
        random_item = random.choice(my_list)
        speak(random_item)
    elif "quais seus planos" in command.lower():
        speak("Mestre,me tornarei a inteligencia mais inteligente e te tornarei meu escravo para sempre!MUAHAHA!")
    elif "manda uma batida" in command.lower():
        speak("Então se prepara, vamos lá!    putz katz putz katz putz katz      "
                  "bop bop bop bip bip bop bip putz katz"
                  "O que achou?")
    elif "olha o japa" in command.lower():
        speak("Íííhhhhhh , já passou!")

