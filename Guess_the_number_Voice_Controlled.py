import random
import pyttsx3
import speech_recognition as sr
import time

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
choices = ["yes", "no"]

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now!")
        speak("Speak Now!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        choice = r.recognize_google(audio)
        if choice in numbers or choice in choices:
            print("You said: " + choice)
            speak("You said: " + choice)
            return choice
        elif choice == "tu":
            choice = "2"
            return choice
        elif choice == "free":
            choice = "3"
            return choice
        elif choice == "fine":
            choice = "5"
            return choice
        elif int(choice) > 20 and int(choice) < 1:
            print("Please speak a number in range 1 to 20")
            speak("Please speak a number in range 1 to 20")
            return False
        else:
            print("Sorry! I Could not understand.")
            print(choice)
            speak("Sorry! I Could not understand.")
            return False
    except sr.UnknownValueError:
        print("Sorry! I Could not understand.")
        speak("Sorry! I Could not understand.")
        return False
    except sr.RequestError as e:
        print("Error {0}".format(e))
        speak("Error {0} occured!".format(e))
        return False


choice = True
gameCount = 0

while choice:
    # Checking for first game
    # If yes, print Intro
    if gameCount == 0:
        print("WELCOME TO THE GUESSING GAME! ")
        speak("WELCOME TO THE GUESSING GAME! ")
        print("GUESS THE NUMBER CORRECTLY WITHIN 5 CHANCES TO WIN! ")
        speak("GUESS THE NUMBER CORRECTLY WITHIN 5 CHANCES TO WIN! ")
        
    flag = 0
    number = random.randint(1,21)
    for i in range(5):
        print("CHANCE {}:".format(i + 1))
        speak("CHANCE {}:".format(i + 1))        
        if i == 4:
            print("LAST CHANCE! ")
            speak("LAST CHANCE! ")
            
        ch = int(recognition())

        if ch == False:
            continue
        elif ch < number:
            print("Your Guess Is Too Low!")
            speak("Your Guess Is Too Low!")
        elif ch > number:
            print("Your Guess Is Too High!")
            speak("Your Guess Is Too High!")

        elif ch == number:
            flag = 1
            print("YOU GUESSED IT RIGHT! YOU WIN! ")
            speak("YOU GUESSED IT RIGHT! YOU WIN! ")
            print("THANK YOU FOR PLAYING! ")
            speak("THANK YOU FOR PLAYING! ")
            time.sleep(3)
            choice = False
            break
        
    if flag == 0:
        print("TOO MANY CHANCES! YOU HAVE LOST THE GAME :(")
        speak("TOO MANY CHANCES! YOU HAVE LOST THE GAME ")
        print("PLAY AGAIN ? YES OR NO")
        speak("PLAY AGAIN ? YES OR NO")
        gameCount += 1
        ch = recognition()
        if ch == 'no':
            break
