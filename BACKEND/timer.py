import time
import pyttsx3

class timer:
    @staticmethod
    def speak(audio):
        engine= pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(audio)
        engine.runAndWait()

    def __init__(self,hours,minutes=0,seconds=0):
        self.hours= float(hours)
        self.minutes= float(minutes)
        self.seconds= float(seconds)

        sleep_value= self.hours*3600+ self.minutes*60+self.seconds

        time.sleep(sleep_value)
        self.speak('Timer Ended')
        time.sleep(.1)
        self.speak('Timer Ended')
        time.sleep(.1)
 

            


if __name__=='__main__':
    obj= timer(

