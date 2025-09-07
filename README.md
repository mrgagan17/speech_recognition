# speech_recognition


This project is a simple speech recognition tool built with Python using the SpeechRecognition
 library.
It can recognize speech either from:

Microphone input (real-time speech).

Audio files (e.g., .wav format).


Features

Adjusts for ambient noise when using the microphone.

Transcribes spoken words into text using Google’s Speech Recognition API.

Supports .wav audio files for offline transcription.

Easy-to-use command-line menu.


Requirements


Python 3.x

Required libraries:

pip install SpeechRecognition pyaudio


Note: pyaudio may require system-specific installation.
For Windows:

pip install pipwin
pipwin install pyaudio
