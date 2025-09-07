import speech_recognition as sr
import os

def recognize_from_microphone():
    """Recognize speech from microphone input until silence is detected."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening... Speak now!)")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Processing...")
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.WaitTimeoutError:
            print("No speech detected within timeout.")
            return None
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Error with the API request: {e}")
            return None

def recognize_from_file(file_path):
    """Transcribe speech from an audio file."""
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return None
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print(f"Processing audio file: {file_path}")
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print("Transcription:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Error with the API request: {e}")
            return None

def main():
    """Main function to run the speech recognition program."""
    while True:
        print("\nSpeech Recognition Menu:")
        print("1. Recognize speech from microphone")
        print("2. Transcribe audio file")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            recognize_from_microphone()
        elif choice == "2":
            file_path = input("Enter the path to the WAV audio file (e.g., audio_files/sample.wav): ")
            recognize_from_file(file_path)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()