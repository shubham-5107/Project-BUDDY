# Project BUDDY

Project BUDDY is a Python-based voice assistant that listens to user commands and performs various desktop automation tasks such as opening websites, setting timers, performing calculations, and running daily routines.
The assistant uses speech recognition to understand commands and text-to-speech to respond, creating a simple interactive assistant for everyday tasks.

---

## Features

* Voice command recognition using a microphone
* Voice responses using text-to-speech
* Open websites through voice commands
* Start timers using natural language
* Perform basic mathematical calculations
* Run automated daily routines
* Dynamic backend module execution

---

## How It Works

1. The assistant listens for voice input through the microphone.
2. Speech is converted into text using the SpeechRecognition library.
3. The command is processed by the program.
4. Based on the command, the assistant performs the action.
5. The assistant responds using voice output.

---

## Technologies Used

* Python
* pyttsx3
* SpeechRecognition
* Webbrowser
* Subprocess
* OS module

---

## Project Structure

```
Project-BUDDY
│
├── main.py
├── BACKEND
│   ├── start_my_day.py
│   └── timer.py
│
├── cache_start_my_day.py
├── cache_timer.py
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/shubham-5107/Project-BUDDY.git
cd Project-BUDDY
```

Install required dependencies:

```
pip install pyttsx3 SpeechRecognition pyaudio
```

---

## Running the Assistant

Run the main Python script:

```
python main.py
```

The assistant will start listening for commands.

---

## Example Voice Commands

```
hello
start my day
open website youtube on Chrome
set timer 2 minutes
what is 5 + 7
go to sleep
```

---

## Future Improvements

* Add conversational AI capability
* Add more desktop automation commands
* Add weather and news updates
* Implement a wake word
* Add graphical user interface
* Improve natural language processing

---

## Author

SHUBHAM SHARMA

GitHub Repository:
https://github.com/shubham-5107/Project-BUDDY
