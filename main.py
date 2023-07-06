import json
import re
import random_responses
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyaudio

bot_name = "Mia"


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("Hello")

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning sweet heart")
        print("Hello,Good Morning sweet heart")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon sweet heart")
        print("Hello,Good Afternoon sweet heart")
    else:
        speak("Hello,Good Evening sweet heart")
        print("Hello,Good Evening sweet heart")

#wishMe()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-us')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant Mia")
speak("Loading your AI personal assistant Mia")


# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        #print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()

def application_msg_parser(user_input):
#hile True:
    #print("You: ")
    #user_input = takeCommand()
    #user_input = input("You: ")
        response = get_response(user_input)

        if 'Youtube opening' in response:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'wikipedia' in response:
            speak('Searching Wikipedia...')
            user_input = user_input.replace("wikipedia", "")
            results = wikipedia.summary(user_input, sentences=3)
            speak("According to Wikipedia")
            speak(results)
            return(results)

        elif 'github opening' in response:
            webbrowser.open_new_tab("https://www.github.com")
            speak("Github is open now")
            time.sleep(5)

        elif 'gmail opening' in response:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'current time' in response:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'search_this_69' in response:
            statement = user_input.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'question' in response:
            statement = user_input.replace("question", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        #elif 'question' in response:
            #speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            #question = takeCommand()
            #app_id = "X9R6L7-4WYATQWJ9V"
            #client = wolframalpha.Client('R2K75H-7ELALHR35X')
            #res = client.query(user_input)
            #answer = next(res.results).text
            #speak(answer)
            #print(answer)

        elif "weather" in response:
            api_key = "3e826e0f9e9479c77abab338620624bd"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            #city_name = input()
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature = current_temperature - 273.15
                current_temperature = int(current_temperature)
                #current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                speak("It will be about " +str(current_temperature) +" Celcius"
                      "\n And you can say it's a " +
                      str(weather_description))
                return ("It will be about " + str(current_temperature) + "Celcius"
                # +"\n humidity (in percentage) = " +
                # str(current_humidiy) +
                                                                         "\n And you can say it's a " +
                        str(weather_description))

        elif "shut down" in response:
            speak("Ok , your pc will log off in 10 sec make sure to exit from every task bro")
            subprocess.call(["shutdown", "/l"])

        else:
            speak(response)
            engine.runAndWait()
            return response