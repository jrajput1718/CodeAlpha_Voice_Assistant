
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    return query


if __name__ == '__main__':
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
    speak("welcome to voice assistant")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
    
        elif 'Hi'in query:
            speak("hello")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")        
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = take_command()
            speak("Thanks for naming me")
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
        elif 'show date and time'in query:
            speak("today's date and time :")
            x=datetime.datetime.now()
            print(x)    
        elif "weather" in query:           
            # Google Open weather website
            # to get API of Open weather
            api_key="c5219b1acceb40b2beed0e1c04ba7d40"
            base_url="http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = take_command()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()   
            if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " +str(current_temperature) + "\n atmospheric pressure (in hPa unit)=" + str(current_pressure) +"\n humidity (in percentage)= " + str(current_humidity) +"\n description= " + str(weather_description))
            else:
                    speak(" City Not Found ")   
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")                   
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open chrome' in query:
            speak("opening chrome")
            webbrowser.open("chrome.com")    
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("web.whatsapp.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'linkedin' in query:
            speak("opening linkedin")
            webbrowser.open("linkedin.com") 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com") 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow")
            webbrowser.open("stackoverflow.com")    
        elif 'stop' in query:
            exit(0)     
            #install-->pip install pyttsx3
            #install-->pip install wikipedia
            #install-->pip install  SpeechRecognition
            #install-->pip install PyAudio
            