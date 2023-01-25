import pyttsx3 #text to speech
from datetime import datetime #for current date nd time
import speech_recognition as sr #for user recognition of voice
import wikipedia # for search egnine form wikiperdia
import webbrowser #for opening any website on web
import pytz #for country time zones
import pyaudio # recording our voice
import pywhatkit #for different features in whatsapp and youtube
from googlesearch import search # for search through google
from word2number import w2n #for converting word as text to number
import math #for math operations
from playsound import playsound #for playing audio
import random as rd #for random songs
import sys #for closing system
import os #removing or adding directory
from tkinter import *
from PIL import  Image,ImageTk #python imaging library for jpg images
import time #for time sleep
import pyjokes #for jokes



main_interface=Tk()
# for Alpromav Speaking
engine= pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
voice_rate= engine.getProperty('rate')
engine.setProperty("rate",voice_rate-10)
# print(voice_rate)
# print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def missasma():
    speak('Miss Asma teaches Programming Language Subject to Software Engineering students')
    speak("she is the reason i was made")
    speak("To the world you may be a teacher")
    speak("but to us you are like the big star shining out there")
    speak("you are the only reason we study python diligently")
    speak("thanks for being our teacher")
    speak("GURU-Ji")
#for wishing
def greetings():
    current_time= int(datetime.now().hour)
    if 0<=current_time<=12:
        speak("good morning")
    elif 12<=current_time<=18:
        speak("Khushamdiid")
    else:speak("Good night ")


# for taking command for user
 #takes voice input from user and converts into string
def command_input():
    playsound("C:\\Users\\cz 3\\Downloads\\final (online-audio-converter.com).mp3")
    a= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        a.pause_threshold = 0.8
        a.energy_threshold = 300
        with sr.Microphone() as source:
            print('say something')
            audio =  a.listen(source=source, timeout=5,phrase_time_limit=6)
            playsound("C:\\Users\\cz 3\Downloads\\final2 (online-audio-converter.com).mp3")
    try:
        print("recognizing")
        user_query=a.recognize_google(audio,language="eng-in")
        print(f"you mean:{user_query}")
    except Exception as e:
        speak("plz repeat, your command is not recognize")
        return "None"
    return user_query

# output display function
def worldclock():
    speak("i can tell you the time of following countries")
    country_names = ["Africa","America","Bangladesh","Dubai","Afghanistan","China","Canada ","Pakistan",
                     "Saudia Arabia","United Kingdom"]
    output.delete("1.0",END)
    output.insert(INSERT, country_names)
    output.update()
    print(country_names)
    speak("Now tell me your choice")

def jokes():
    my_jokes = pyjokes.get_joke(language="en", category="all")
    output.delete("1.0",END)
    output.insert(INSERT,my_jokes)
    output.update()
    print(my_jokes)
    speak(my_jokes)

def best_websites(x):
    speak("these are the best result for your required search")
    for website in search(x, num=5, stop=10, pause=2):
        output.delete("1.0", END)
        output.insert(INSERT, website)
        output.update()
        print(website)

def calcdisplay():
    operation = ['addition','subtraction','multiplication','division','angles through trignometric ']
    output.delete("1.0", END)
    output.insert(INSERT,operation)
    output.update()
    print(operation)

def addition(x,y):
    try:
        c = w2n.word_to_num(x)
        print(c)
        output.delete("1.0", END)
        output.insert(INSERT, c)
        output.update()
        d = w2n.word_to_num(y)
        print(d)
        output.delete("1.0", END)
        output.insert(INSERT,d)
        output.update()
        answer = c + d
        output.delete("1.0", END)
        output.insert(INSERT, answer)
        output.update()
        speak(f"your answer is {answer}")
        print(answer)
    except ValueError as e:
        speak("unable to recognize,try again")
    
def subtraction(x,y):
    try:
        c = w2n.word_to_num(x)
        print(c)
        output.delete("1.0", END)
        output.insert(INSERT, c)
        output.update()
        d = w2n.word_to_num(y)
        print(d)
        output.delete("1.0", END)
        output.insert(INSERT, d)
        output.update()
        answer = c - d
        output.delete("1.0", END)
        output.insert(INSERT, answer)
        output.update()
        speak(f"your answer is {answer}")
        print(answer)
    except ValueError as e:
        speak("unable to recognize,try again")

def multiplication(x,y):
    try:
        c = w2n.word_to_num(x)
        print(c)
        output.delete("1.0", END)
        output.insert(INSERT, c)
        output.update()
        d = w2n.word_to_num(y)
        print(d)
        output.delete("1.0", END)
        output.insert(INSERT, d)
        output.update()
        answer = c*d
        output.delete("1.0", END)
        output.insert(INSERT, answer)
        output.update()
        speak(f"your answer is {answer}")
        print(answer)
    except ValueError as e:
        speak("unable to recognize,try again")
    
def division(x,y):
    try:
        c = w2n.word_to_num(x)
        print(c)
        output.delete("1.0", END)
        output.insert(INSERT, c)
        output.update()
        d = w2n.word_to_num(y)
        print(d)
        output.delete("1.0", END)
        output.insert(INSERT, d)
        output.update()
        answer = c/d
        output.delete("1.0", END)
        output.insert(INSERT, answer)
        output.update()
        speak(f"your answer is {answer}")
        print(answer)
    except ValueError as e:
        speak("unable to recognize,try again")
def sinQ(x):
    try:
        c = w2n.word_to_num(x)
        answer4 = '%.3f' % (math.sin(c))
        output.delete("1.0", END)
        output.insert(INSERT, answer4)
        output.update()
        speak(f"sin{c} is {answer4} radian ")

    except ValueError as e:
        speak("unable to recognize,try again")

def cosQ(x):
    try:
        c = w2n.word_to_num(x)
        answer5 = '%.3f' % (math.cos(c))
        output.delete("1.0", END)
        output.insert(INSERT, answer5)
        output.update()
        speak(f"cos{c} is {answer5} radian ")
    except ValueError as e:
        speak("unable to recognize,try again")


def tanQ(x):
    try:
        c = w2n.word_to_num(x)
        answer5 = '%.3f' % (math.tan(c))
        output.delete("1.0", END)
        output.insert(INSERT, answer5)
        output.update()
        speak(f"tan{c} is {answer5} radian ")

    except ValueError as e:
        speak("unable to recognize,try again")


def livesaving():
    output.delete("1.0", END)
    output.insert(INSERT,"you are allowed to feel messed up and inside out It doesn't mean you are defective, it means you are human")
    output.update()
    speak("you are allowed to feel messed up and inside out It doesn't mean you are defective, it means you are human")
    output.insert(INSERT,"\nif today all you did was hold yourself, i'm proud of you")
    output.update()
    speak("if today all you did was hold yourself, i'm proud of you")
    output.insert(INSERT,"\n Once you choose hope, anything is possible")
    output.update()
    speak(" Once you choose hope, anything is possible")




def main_program():
    greetings()

    speak("Welcome")
    speak("Alpro mav is at your service. How may I help you?")
    ''' All the commands said by user will be stored here in 'query' and will be converted to lower case for easily
           recognition of command'''
    while True:
        user_query = command_input().lower()
        # creating logics for our various task
        if 'tell me about yourself' in user_query or 'your introduction' in user_query:
            speak(
                "Hi!Nice to meet you. I am Alpro mav and I am made by Mavra and Aleeza. I am here to help you.To say any command, click speak button")

        elif "what's your name" in user_query or "what is your name" in user_query:
            speak("My friends call me Alpro mav")

        elif "wikipedia" in user_query:
                try:
                    speak("What do you want from wikipedia?")
                    inst=command_input().lower()
                    user_query=user_query.replace("wikipedia"," ")
                    speak("Getting to wikipedia..")
                    results= wikipedia.summary(inst,sentences= 1)
                    wikipedia
                    speak("According to Wikipedia")
                    output.delete()
                    output.insert(INSERT,results)
                    output.update()
                    speak(results)
                except Exception as e:
                   speak("Wikipedia doesnot have infromation related to "+inst)

        elif 'joke' in user_query or 'tell me a joke' in user_query:
            jokes()

        elif 'open youtube' in user_query or 'utube' in user_query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")
            time.sleep(5)

        elif 'google' in user_query or 'googli' in user_query:
            speak("opening google")
            webbrowser.open("https://www.google.com/")
            time.sleep(5)

# current timne
        elif 'time' in user_query or "now " in user_query:
            # time=datetime.datetime.now().strftime("%H-%M minutes %S seconds")
            time1 = datetime.now().strftime("%H:%M:%S")
            speak(f"The time now is" + time1)
# current date
        elif 'date' in user_query:
            date = datetime.now().strftime("%d/%m/%y")
            speak("The date today is" + date)

        elif 'Open code' in user_query or 'vs code' in user_query:
            speak("opening Vs code")
            ProgramPath1 = "C:\\Users\\cz 3\Desktop\\Visual Studio Code.lnk"
            os.startfile(ProgramPath1)
            time.sleep(5)

        elif 'Open notepad' in user_query or 'notepad' in user_query or 'note' in user_query:
            speak("opening notepad")
            os.system("Notepad")
            time.sleep(5)

        elif 'open netflix' in user_query:
            speak("opening netflix")
            webbrowser.open("https://www.netflix.com/pk/")
            time.sleep(5)

        elif 'open gmail' in user_query or 'mail' in user_query or 'male' in user_query:
            speak("opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/")
            time.sleep(5)


        elif 'open stackoverflow' in user_query or 'overflow' in user_query:
            speak("opening stackoverflow")
            webbrowser.open("https://stackoverflow.com/")
            time.sleep(5)

        elif 'Open github' in user_query or 'git hub' in user_query:
            speak("opening github")
            webbrowser.open("https://github.com/")
            time.sleep(5)

        
        elif 'open weather' in user_query or 'weather now' in user_query:
            speak("opening weather on google")
            webbrowser.open('''https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-
            ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..
            35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..''')
            time.sleep(5)

# for time zone in different countries
        elif  "country " in user_query or  "different" in user_query:
            worldclock()


        elif 'dubai' in user_query or 'dubaai' in user_query:
            dubai_tz = pytz.timezone('Asia/Dubai')
            current_time_dubai = datetime.now(dubai_tz)
            print(f'The current time in Dubai is {current_time_dubai.strftime("%H:%M:%S")}')
            speak(f'The current time in Dubai is {current_time_dubai.strftime("%H:%M:%S")}')

        elif 'america' in user_query or 'ameerica' in user_query:
            america_tz = pytz.timezone('America/New_York')
            current_time_america = datetime.now(america_tz)
            print(f'The current time in America is {current_time_america.strftime("%H:%M:%S")}')
            speak(f'The current time in America is {current_time_america.strftime("%H:%M:%S")}')

        elif 'africa' in user_query or 'africa' in user_query:
            africa_tz = pytz.timezone('Africa/Cairo')
            current_time_africa = datetime.now(africa_tz)
            print(f'The current time in Africa is {current_time_africa.strftime("%H:%M:%S")}')
            speak(f'The current time in Africa is {current_time_africa.strftime("%H:%M:%S")}')

        elif 'bangladesh' in user_query or 'baangladesh' in user_query:
            bangladesh_tz = pytz.timezone('Asia/Dhaka')
            current_time_bangladesh = datetime.now(bangladesh_tz)
            print(f'The current time in Bangladesh is {current_time_bangladesh.strftime("%H:%M:%S")}')
            speak(f'The current time in Bangladesh is {current_time_bangladesh.strftime("%H:%M:%S")}')

        elif 'afghanistan' in user_query or 'afghan' in user_query:
            afghanistan_tz = pytz.timezone('Asia/Kabul')
            current_timeafghanistan = datetime.now(afghanistan_tz)
            print(f'The current time in afghanistan is {current_timeafghanistan.strftime("%H:%M:%S")}')
            speak(f'The current time in afghanistan is {current_timeafghanistan.strftime("%H:%M:%S")}')

        elif 'china' in user_query or 'Chinaa' in user_query:
            china_tz = pytz.timezone('Asia/Shanghai')
            current_time_china = datetime.now(china_tz)
            print(f'The current time in china is {current_time_china.strftime("%H:%M:%S")}')
            speak(f'The current time in china is {current_time_china.strftime("%H:%M:%S")}')

        elif 'australia' in user_query or 'austraalia' in user_query:
            australia_tz = pytz.timezone('Australia/Sydney')
            current_time_australia = datetime.now(australia_tz)
            print(f'The current time in australia is {current_time_australia.strftime("%H:%M:%S")}')
            speak(f'The current time in australia is {current_time_australia.strftime("%H:%M:%S")}')

        elif 'pakistan' in user_query or 'karachi' in user_query:
            pakistan_tz = pytz.timezone('Asia/Karachi')
            current_time_pakistan = datetime.now(pakistan_tz)
            print(f'The current time in pakistan is {current_time_pakistan.strftime("%H:%M:%S")}')
            speak(f'The current time in pakistan is {current_time_pakistan.strftime("%H:%M:%S")}')

# whatsapp sending messages
        elif "message" in user_query or "whatsapp" in user_query:
            speak("who do you want to message")
            a = int(datetime.now().hour)
            b = int(datetime.now().minute) + 2
            reciever = command_input().lower()
            speak("kindly tell me your message")
            chat = command_input().lower()

            if "mama" in reciever or 'mom' in reciever or "mommy" in reciever:
                send_to = "+923213226078"
                pywhatkit.sendwhatmsg(send_to, chat, a, b)
                speak("sending message")
                time.sleep(5)

            elif "friend" in reciever or "mavra" in reciever or "partner" in reciever or "class fellow" in reciever:
                send_to = "+923326287222"
                pywhatkit.sendwhatmsg(send_to, chat, a, b)
                speak("sending message")
                time.sleep(5)
            else:
                speak("Number not recognized.")

#languages
        elif "eid mubarak " in user_query or "5 language" in user_query:
            with open("C:\\Users\cz 3\\PycharmProjects\\pythonProject1\\alllanguage.txt") as f:
                for i in f.readlines():
                    speak(i)

#search on google
        elif 'search' in user_query or 'search on google' in user_query:
            speak("What do you want me to search")
            user_query2 = command_input().lower()
            speak("opening searches for" + user_query2)
            pywhatkit.search(user_query2)
            time.sleep(5)

# on yt play song
        elif 'play songs' in user_query or "online" in user_query:
            # on yt play song
            # song=query.replace('play',"")
            speak("Which song you want to play")
            song = command_input().lower()
            speak("Playing" + song + "On youtube")
            pywhatkit.playonyt(song)
            time.sleep(5)

# google search engine
        elif "bestwebsite" in user_query or "links" in user_query or "blinks" in user_query:
            speak("what do you want me to search")
            user_query2 = command_input().lower()
            best_websites(user_query2)

        elif "simple" in user_query or "calculator" in user_query:
            speak("i can only perform following calculation")
            calcdisplay()

        elif "add " in user_query or "addition" in user_query:
            speak("tell me your first number")
            user_query3 = command_input().lower()
            speak("tell me your 2nd number")
            user_query4 = command_input().lower()
            addition(user_query3,user_query4)

        elif "subtract" in user_query or "subtraction" in user_query or "minus" in user_query:
            speak("tell me your first number")
            user_query3 = command_input().lower()
            speak("tell me your 2nd number")
            user_query4 = command_input().lower()
            subtraction(user_query3,user_query4)

        elif "multiply" in user_query or "product" in user_query or "multiplication" in user_query:
            speak("tell me your first number")
            user_query3 = command_input().lower()
            speak("tell me your 2nd number")
            user_query4 = command_input().lower()
            multiplication(user_query3,user_query4)


        elif "division" in user_query or "divide" in user_query or "divided" in user_query:
            speak("tell me your first number")
            user_query3 = command_input().lower()
            speak("tell me your 2nd number")
            user_query4 = command_input().lower()
            division(user_query3,user_query4)
            
        elif "sign" in user_query or "sign theta" in user_query:
            speak("tell me your angle")
            user_query3 = command_input().lower()
            sinQ(user_query3)

        elif "cost" in user_query or "cosine" in user_query:
            speak("tell me your angle")
            user_query3 = command_input().lower()
            cosQ(user_query3)

            
        elif "ten" in user_query or "angle" in user_query:
            speak("tell me your angle")
            user_query3 = command_input().lower()
            tanQ(user_query3)
                
# live saving
        elif "suicide" in user_query or "kill" in user_query or "depression" in user_query:
            a = int(datetime.now().hour)
            b = int(datetime.now().minute) + 2
            livesaving()
            pywhatkit.sendwhatmsg("+923213226078", "your child may do something dangerous. Go and check on him or her",
                                  a, b)

#  for offline music
        elif " music" in user_query or "any" in user_query:
            music_dir = "C:\\Users\\cz 3\\Desktop\\My Docs\\mysongs"
            songs = os.listdir(music_dir)
            print(songs)
            l1 = [0, 1, 2, 3]
            number = rd.choice(l1)
            os.startfile(os.path.join(music_dir, songs[number]))
            time.sleep(18)

# stop or exit
        elif "stop" in user_query or "goodbye" in user_query:
            speak("time for me to leave good luck")
            sys.exit()

        

main_interface.title("ALproMav")
main_interface.geometry("1920x1200")
main_interface.maxsize(1920,1200)
main_interface.minsize(1920,1200)
bg_frame= Frame(main_interface).place(x=150,y=130)
bg= Image.open("D:\\parhley behan\\DATABASE\\image (1).jpg")
bg1=ImageTk.PhotoImage(bg)
bg_label= Label(bg_frame,image=bg1)
bg_label.place(x=0,y=0)


#main heading
Label(main_interface,text="ALproMAV",bg="#000117",fg="#06D9FF",font="Algerian 60",relief=RAISED,border=0,width=10).place(x=20,y=100)
#side heading
Label(main_interface,text="Engine of Change",bg="#000117",fg="white",font="Constantia 26 italic",relief=RIDGE,border=0,width=14).place(x=320,y=235)
btn_img= Image.open("D:\\parhley behan\\DATABASE\\waves2.jpg")
btn_img1=ImageTk.PhotoImage(btn_img)
#microphone 
b2= Button(main_interface,image=btn_img1,text="click here",font="Constantia 17",fg="white",bg="black",border=0,relief=RAISED,command=lambda :main_program())
b2.place(x=300,y=350)
b3=Button(main_interface,text="Open with Smile",bg="#000110",fg="white" , relief=RAISED,font="Constantia 13 bold",borderwidth=10,width=15,command= lambda : missasma()).place(x=320,y=580)
#introlabel
Label(main_interface,text="Made By :\n Aleeza Hussain(SE 22018)",font="Constantia 14",bg="#000110",fg="#06D9FF",width=30,border=0).place(x=1350,y=830)
#output display
output= Text(main_interface,wrap="word",width=32,height=8,bg="#000110",fg="#06D9FF",font="Constantia 14 ",relief=SUNKEN,border=8)
output.place(x=150,y=660)


main_interface.mainloop()


