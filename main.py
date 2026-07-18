import pyttsx3, speech_recognition as sr
import time, webbrowser, subprocess, threading

class GreetingSkill:
    def matches(self, query):
        return "hello" in query.split()
    
    def handle(self, query):
        return "Hello shubham sir"

class StartMyDaySkill:
    def matches(self, query):
        return "start my day" == query
    
    def handle(self, query):
        from SKILLS import start_my_day as smd
        return smd.start_my_day().report

class TimerSkill:
    def matches(self, query):
        return 'set' in query.split() and 'timer' in query.split() or 'start' in query.split() and 'timer' in query.split()
    
    def handle(self, query):
        from SKILLS import timer
        t= timer.timer()
        duration= t.paraphraser(query)
        threading.Thread(target= t.buzzer, args=(duration, ), daemon=True).start()
        return ""

class WebLauncherSkill:
    def matches(self, query):
        return 'website' in query.split() and 'Chrome' in query.split()
    
    def handle(self, query):
        root_domain= query.split('website')[-1].split('on')[0].replace(' ','')
        webbrowser.open(f'www.{root_domain}.com')
        return ""


class ExitSkill:
    def matches(self, query):
        return 'go to sleep' ==query or 'you may rest now buddy' == query
    
    def handle(self, query):
        quit()


def speak(audio):
    engine= pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(1)
        print('Listening')
        speak('Listening')
        
        r.pause_threshold= 1.5
        audio= r.listen(source)

    try:
        query= r.recognize_google(audio, language= 'en-in')
            
    except Exception as e:
        print('Sorry. can you say that again sir...')
        speak('Sorry. can you say that again sir...')
        return ''
    return query

skills= [GreetingSkill(),
             StartMyDaySkill(), 
             TimerSkill(),
             WebLauncherSkill(),
             ExitSkill()]

def processor(query):
    print('admin:', query)

    if query=="":
        return " "

    for skill in skills:
        if skill.matches(query):
            return (skill.handle(query))
    
    return "Sorry sir i can't help you with it at this point of time. can i help you with something else??"
        


if __name__=='__main__':
    while True:
        response= processor(take_command())
        print(response)
        speak(response)
