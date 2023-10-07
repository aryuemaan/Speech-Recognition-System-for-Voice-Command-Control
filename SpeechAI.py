import speech_recognition as sr

class SpeechRecognitionSystem:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)
        return audio

    def recognize(self, audio):
        try:
            text = self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            return "Could not recognize speech: {0}".format(e)
        return text

    def control_device(self, command):
        # This function would implement the logic for controlling the device based on the given command.
        # For example, if the command is "turn on the light", the function would send a signal to the light to turn it on.
        pass

def main():
    srs = SpeechRecognitionSystem()

    while True:
        audio = srs.listen()
        text = srs.recognize(audio)

        if text is not None:
            print("You said: {}".format(text))
            srs.control_device(text)

if __name__ == "__main__":
    main()
