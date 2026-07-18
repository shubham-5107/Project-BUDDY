# Project BUDDY

Project BUDDY is a Python-based voice assistant for desktop automation. It listens to voice commands, processes them through a modular skill-based system, and responds using text-to-speech — creating a simple, interactive assistant for everyday tasks.

> **Version:** v2 — a refactor of the core engine toward a cleaner, modular, skill-based architecture.

---

## Table of Contents

- [Features](#features)
- [What's New in v2](#whats-new-in-v2)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Skills](#skills)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Example Voice Commands](#example-voice-commands)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Features

- Voice command recognition using a microphone
- Voice responses using text-to-speech
- Website launcher via voice commands
- Natural-language voice-controlled timer
- Daily routine with live time and weather report
- Modular, skill-based command handling

---

## What's New in v2

v2 is a structural refactor of the core engine. Key changes:

| Area | v1 | v2 |
|---|---|---|
| Command routing | Single `match/case` block | Independent `Skill` classes with `matches()` / `handle()` |
| Backend imports | File-copy workaround (`gods` class) into cache files | Direct import from a proper `SKILLS` package |
| Timer execution | Spawned as a subprocess (`subprocess.Popen`) via a cache file | Runs on a background daemon thread |
| Voice output | Backend modules (`timer.py`, `start_my_day.py`) called `pyttsx3` directly | Backend modules return data only; `main.py` is the sole place that speaks |
| Dependencies | Included unused imports (e.g. `os`) | Trimmed to only what's needed |

> **Note:** The calculator skill (`what is 5 + 7`) from v1 has not yet been ported to the new architecture and is planned for a future update.

---

## How It Works

1. `take_command()` listens via the microphone and transcribes speech to text using `SpeechRecognition`.
2. `processor()` checks the query against a list of registered `Skill` instances.
3. The first `Skill` whose `matches()` returns `True` handles the query via `handle()` and returns a response string.
4. `speak()` converts the response to audio output.

---

## Project Structure

```
Project-BUDDY
│
├── main.py                 # Entry point: command loop, Skill registry, dispatch logic
├── SKILLS/
│   ├── start_my_day.py     # Daily greeting + date/time + weather report
│   └── timer.py            # Timer parsing (paraphraser) and execution (buzzer)
│
├── requirements.txt
└── README.md
```

---

## Skills

### `GreetingSkill`
Matches queries containing `"hello"` and responds with a greeting.

### `StartMyDaySkill`
Matches the exact phrase `"start my day"`. Builds a spoken report combining:
- Time-based greeting (Morning / Afternoon / Evening / night)
- Current date and time
- Live temperature and weather description (fetched from `wttr.in`)

### `TimerSkill`
Matches queries containing `"set"`/`"start"` and `"timer"`. Parses the spoken duration via `timer.paraphraser()`, then runs `timer.buzzer()` on a background thread so the assistant stays responsive while counting down.

### `WebLauncherSkill`
Matches queries containing `"website"` and `"Chrome"`. Extracts the domain from the query and opens `www.<domain>.com` in the default browser.

### `ExitSkill`
Matches `"go to sleep"` or `"you may rest now buddy"` and exits the program.

---

## Technologies Used

- **Python** 3.08
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) — text-to-speech
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/) — voice-to-text
- [`requests`](https://pypi.org/project/requests/) — weather data
- `webbrowser`, `threading`, `subprocess` — standard library

---

## Installation

Clone the repository:

```bash
git clone https://github.com/shubham-5107/Project-BUDDY.git
cd Project-BUDDY
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

> `SpeechRecognition`'s `Microphone` support requires `PyAudio`. If the wheel doesn't install cleanly, you may need your OS package manager (e.g. `sudo apt install portaudio19-dev` on Linux) before retrying `pip install pyaudio`.

---

## Usage

Run the main script:

```bash
python main.py
```

The assistant will start listening for commands after printing/saying **"Listening"**.

---

## Example Voice Commands

- `hello`
- `start my day`
- `open website youtube on Chrome`
- `set timer for 2 minutes`
- `go to sleep`

---

## Known Limitations

- Calculator skill from v1 is not yet ported to the new architecture.
- Timer alerts print to console rather than being spoken, since `pyttsx3` is not reliably thread-safe when called from a background thread.
- Weather report uses a hardcoded location rather than detecting the user's location.
- Limited error handling around network calls (weather fetch, speech recognition).

---

## Future Improvements

- [ ] Re-add the calculator skill using the new `Skill` class interface
- [ ] Add conversational AI capability
- [ ] Add more desktop automation commands
- [ ] Add news updates
- [ ] Implement a wake word
- [ ] Add a graphical user interface
- [ ] Improve natural language processing
- [ ] Configurable location for weather reports
- [ ] Thread-safe spoken alert for the timer

---

## Author

**Shubham Sharma**

GitHub Repository: [Project-BUDDY](https://github.com/shubham-5107/Project-BUDDY)
