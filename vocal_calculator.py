import speech_recognition as sr
import pyttsx3
import re

# Initialize the recognizer and the speaker
recognizer = sr.Recognizer()
speaker = pyttsx3.init()

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)
        print("Audio received")
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error connecting to the speech recognition service.")
            speak("Sorry, there was an error connecting to the speech recognition service.")
            return None

def calculate(expression):
    try:
        # Evaluate the mathematical expression
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error in calculation: {e}")
        speak("Sorry, there was an error in the calculation.")
        return None

def ask_to_continue():
    speak("Do you want to perform another calculation? Say 'yes' to continue or 'no' to exit.")
    response = get_audio()
    if response:
        response = response.lower()
        if 'yes' in response:
            return True
        elif 'no' in response:
            return False
        else:
            speak("I didn't catch that. Please say 'yes' or 'no'.")
            return ask_to_continue()
    return False

def main():
    speak("Welcome to the voice calculator. Say a mathematical expression to calculate.")
    
    while True:
        expression = get_audio()
        if expression:
            # Remove non-mathematical characters to avoid security issues
            expression = re.sub(r'[^\d+\-*/(). ]', '', expression)
            result = calculate(expression)
            if result is not None:
                result_text = f"The result is {result}"
                print(result_text)
                speak(result_text)
        
        # Ask if the user wants to perform another calculation or exit
        if not ask_to_continue():
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
