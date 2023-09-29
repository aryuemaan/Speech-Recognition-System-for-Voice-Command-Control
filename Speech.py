#pip install SpeechRecognition

import speech_recognition as sr

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)  # Use Google Web Speech API for recognition
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
        return None

def main():
    while True:
        command = recognize_speech()
        if command:
            if command == "exit":
                print("Exiting...")
                break
            else:
                # Add your custom logic based on recognized commands
                print(f"Executing command: {command}")

if __name__ == "__main__":
    main()
