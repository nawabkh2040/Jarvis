import speech_recognition as sr
import os 
import webbrowser
import pyttsx3
import openai
from gtts import gTTS
import datetime
from config import apikey
import random
import requests
from selenium import webdriver
import time




def speak_hindi(hindi_l):
     language = 'hi'
     tts = gTTS(text=hindi_l, lang=language, slow=False)
     tts.save("output.mp3")
     os.system("start output.mp3")
     

def speechAudio(qu):
    engine = pyttsx3.init()
    print("Try To Speech")
    rate = engine.getProperty('rate')
#     print(rate)
    engine.setProperty('rate', 125)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
    engine.say(qu)
    print("Is Speaking ")
    engine.runAndWait()
    engine.stop()


def ai(data_j):
     openai.api_key = apikey
     text=f"AI response For Prompt {data_j}\n ****************************************************************\n\n"
     response = openai.Completion.create(
          model="gpt-3.5-turbo-instruct",
          prompt=data_j,
          temperature=1,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
     )
     try:
          print(response["choices"][0]["text"])
          text += response["choices"][0]["text"]
          if not os.path.exists("AI_Gen"):
               os.mkdir("AI_Gen")
          with open(f"AI_Gen/prompt -{random.randint(1,12345455255)}","w") as f:
               f.write(text)
          speechAudio(response["choices"][0]["text"])
     except Exception as e:
          print("Sorry Some issue in chat Gpt")

def Image_gen(image_data):
     openai.api_key = apikey
     response = openai.Image.create(
          prompt=image_data,
          n=1,
          size="1024x1024"
     )
     image_url = response['data'][0]['url']

def listenAudio():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Speak Anything :")
          audio = r.listen(source)
          try:
               print("Recognizing....")
               text = r.recognize_google(audio, language='en-in')
               print("You said : {}".format(text))
               sites = [
                    ["YouTube", "https://youtube.com/"],
                    ["Google", "https://www.google.com/"],
                    ["Facebook", "https://www.facebook.com/"],
                    ["Twitter", "https://twitter.com/"],
                    ["Instagram", "https://www.instagram.com/"],
                    ["LinkedIn", "https://www.linkedin.com/"],
                    ["Reddit", "https://www.reddit.com/"],
                    ["Amazon", "https://www.amazon.com/"],
                    ["life saver QR code", "http://nawabkh2040.pythonanywhere.com/"],
                    ["Netflix", "https://www.netflix.com/"],
                    ["Twitch", "https://www.twitch.tv/"],
                    ["CNN", "https://www.cnn.com/"],
                    ["BBC News", "https://www.bbc.com/news"],
                    ["The New York Times", "https://www.nytimes.com/"],
                    ["Wikipedia", "https://www.wikipedia.org/"],
                    ["GitHub", "https://github.com/"],
                    ["Stack Overflow", "https://stackoverflow.com/"],
               ]
               for site in sites:
                    if f"open {site[0]}" in text.lower() or f"open {site[0]}" in text:
                         speechAudio("Opening "+site[0])
                         webbrowser.open(site[1])
               if f"jarvis exit" in text.lower() or f"Jarvis Exit" in text:
                    speechAudio("Okay By Nawab")
                    return -1
               if f"open chrome" in text.lower() or f"Open Chrome" in text: 
                    filepath="C:\Program Files\Google\Chrome\Application\chrome.exe"
                    os.startfile(filepath)
               if f"open microsoft word" in text.lower() or f"Open Microsoft Word" in text or f"open word" in text.lower(): 
                    filepath="C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE"
                    os.startfile(filepath)
               if f"open microsoft excel" in text.lower() or f"Open Microsoft Excel" in text or f"open excel" in text.lower(): 
                    filepath="C:\\Program Files\\Microsoft Office\\root\Office16\\EXCEL.EXE"
                    os.startfile(filepath)
               if f"open microsoft powerpoint" in text.lower() or f"Open Microsoft Powerpoint" in text or f"open powerpoint" in text.lower(): 
                    filepath="C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE"
                    os.startfile(filepath)
               if f"the time" in text.lower() or f"The Time " in text: 
                    hour=datetime.datetime.now().strftime("%H")
                    minutes=datetime.datetime.now().strftime("%M")
                    second=datetime.datetime.now().strftime("%S")
                    speechAudio(f"Current  time is {hour} Bajke {minutes} minutes  or {second} second")
               if f"using ai" in text.lower() or f"Using AI" in text:
                    search_query = text.split("AI", 1)[1].strip()
                    ai(search_query)
               if f"open browser and search" in text.lower() or f"Open Browser And Search" in text: 
                    search_query = text.split("search for", 1)[1].strip()
                    search_url = f"https://www.google.com/search?q={search_query}"
                    speechAudio("Searching For "+search_query)
                    webbrowser.get('windows-default').open(search_url)
               if f"play song on youtube" in text.lower() or  f"play song on YouTube" in text: 
                    text=text.lower()
                    search_query = text.split("youtube ", 1)[1].strip()
                    search_url = f"https://www.youtube.com/search?q={search_query}"
                    speechAudio("Opening Song In Youtube "+search_query)
                    webbrowser.get('windows-default').open(search_url)
               if f"what is" in text.lower():
                    ai(text) 
               if f"play song" in text.lower() or f"Play Song" in text: 
                    search_query = text.split("song ", 1)[1].strip()
                    base_url = "https://saavn.me/search/songs"
                    params = {
                         "query": search_query,
                         "page": 1,
                         "limit": 2
                    }
                    response = requests.get(base_url, params=params)
                    if response.status_code == 200:
                         data = response.json()
                         songs = data["data"]["results"]
                         if songs:
                              song = songs[0]
                              print(song['url'])
                              webbrowser.get('windows-default').open(song['url'])
                         else:
                              print("No songs found")
                              speechAudio("No songs found")
                    else:
                         print(f"Error making request. Status code: {response.status_code}")
               if f"who is the creator of universe" in text.lower():
                    speechAudio("Allah")
               if f"Assalam Walekum" in text or f" Assalamualaikum " in text or  f" Assalamu Alaikum "  in text or f"assalamu alaikum " in text or f"assalamualaikum" in text.lower():
                    print("Walekum Assalam ")
                    print("वालेकुम अस्सलाम व रहमतुल्लाहि व बरकतुहू")
                    speak_hindi("वालेकुम अस्सलाम व रहमतुल्लाहि व बरकतुहू ")
               # todo: Add More Features
               else:
                    print(text)
                    return text
               
          except Exception as e:
               # sorry="Sorry Please Speak Again"
               # speechAudio(sorry)
               print("Sorry Please Speak Again")
while True:
     qu = listenAudio()
     if qu==-1:
          break
# speechAudio("Allah  subhanahu waa ta'ala")