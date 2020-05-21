import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import datetime
import warnings
import calendar
import wikipedia
import pyttsx3
import random
import subprocess
from webbrowser import open
from WeatherAPP import WeatherInformation
from sys import argv
import webbrowser
import time
# To access clipbord
from pyperclip import paste

# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request

warnings.filterwarnings('ignore')


def name_generator():
    ran = random.randint(1, 1000000)
    ran = str(ran)
    return ran


def speakdata(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def speak(text):
    # tts = gTTS(text=text, lang="en")
    # filename = "voice.mp3"
    # tts.save(filename)
    # playsound.playsound(filename)

    print("in ...................................")
    tts = gTTS(text=text, lang="en", slow=False)
    new_name = name_generator()
    new_name = new_name + ".mp3"
    tts.save(new_name)

    print("saving...............................")
    playsound.playsound(new_name)
    print("saying................................")
    print(text)
    try:
        os.remove(new_name)
    except:
        print("i cant")


def get_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        print('Say something')
        audio = r.listen(source)
    said = ''

    try:
        said = r.recognize_google(audio)
        print("You said : ", said)
    except sr.UnknownValueError:
        speak('I am not able to understand the audio')
    except sr.RequestError as e:
        print('Request results from server error' + e)

    return said


def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]

    monthNum = now.month
    dayNum = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November',
                   'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                      '14th', '15th', '16th', '17th',
                      '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th',
                      '30th', '31st']

    return 'Today is ' + weekday + '  ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + ' .'


def wakeWord(text):
    WAKE_words = ['Hey Sunny', 'Hi Sunny']

    text = text.lower()

    for phrase in WAKE_words:
        if phrase in text:
            return True
    return False


def greeting(text):
    Greetings_Input = ['Hi', 'Hello', 'Hey', 'greetings', 'whatup']

    Greetings_Response = ['howdy', 'whats goodd', ' hello', 'hey there']

    for word in text.split():
        if word.lower() in Greetings_Input:
            return random.choice(Greetings_Response) + '. '
    return ''


def getPerson(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]


def getWeather(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'Temperature' and wordList[i + 1].lower() == 'in':
            return wordList[i + 2] + ' ' + wordList[i + 3]


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["start notepad.exe", file_name])
    #os.system('start notepad.exe')


def media():
    os.system('start groove.exe')


time.sleep(1)
while True:

    text = get_audio()

    response = ''

    if wakeWord(text):
        response = response + ' ' + greeting(text)

    if "hello" in text:
        speak("hello, how are you?")
    elif "what is your name" in text:
        speak("My name is Sunny , What is your name ?")
        text = get_audio()
        # speak(text)
        speak('At your service :' + text)
    elif 'date' in text:
        get_date = getDate()
        response = response + ' ' + get_date
        speak(response)

    elif 'time' in text:
        now = datetime.datetime.now()
        meridian = ''
        if now.hour >= 12:
            meridian = 'p.m'
            hour = now.hour - 12
        else:
            meridian = 'a.m'
            hour = now.hour

        if now.minute < 10:
            minute = '0' + str(now.minute)
        else:
            minute = str(now.minute)

        speak('It is ' + str(hour) + ':' + minute + ' ' + meridian + ' .')

    elif 'who is' in text:
        person = getPerson(text)
        wiki = wikipedia.summary(person, sentences=2)
        response = wiki
        speak(wiki)
    elif 'temperature in' in text:
        print("Hi")
        city_name = getWeather(text)
        Variablee_info = WeatherInformation.get_weather_info(str(city_name))
        speak(Variablee_info)

    elif 'play music' in text:
        speak('What I play for you Sir')
        listen = get_audio()
        os.startfile('F:\krishna/' + listen + '.mp3')
        speak('Ok Sir, Playing' +listen+' for you ')

    elif 'search' in text:
        speak("What do want to search for ?")
        search = get_audio()
        print(search)
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)

    elif 'find location' in text:
        speak("What is the location ?")
        location = get_audio()
        print(location)
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)

    NOTE_STRS = ["make a note", "write this down", "remember this", "type this"]
    for phrase in NOTE_STRS:
        if phrase in text:
            speak("What would you like me to write down? ")
            write_down = get_audio()
            note(write_down)
            speak("I've made a note of that.")

    if "where is" in text:
        text = text.split(" ")
        location = text[2:]
        speak("Hold on Sir, I will show you where " + str(location) + " is.")
        if len(argv) > 1:
            location = " ".join(argv[1:])
        else:
            location = paste()
        open("http://www.google.com/maps/place/" + str(location))
        # speak("I have opened " + str(location) + " location in map, please have look")

    if 'exit' in text:
        exit()

    # speak(text)
