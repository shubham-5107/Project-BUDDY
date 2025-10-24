import pyttsx3
import requests
import datetime
def speak(audio):
    engine= pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()
    
class start_my_day:
    def __init__(self):
            time_value= int(datetime.datetime.now().strftime('%H'))
            greeting_phrase_list= [(0,4,'night'),
                                   (4,12,'Morning'),
                                   (12,17,'Afternoon'),
                                   (17,20,'Evening'),
                                   (20,23.9,'night')
                                   ]
            greeting_phrase= next(greeting for low,high,greeting in greeting_phrase_list if low<=time_value<high)


            
            temperature_value=float(requests.get('https://wttr.in/28.33,80.06?format=3').text.split()[-1].strip('+').strip('°C'))
            
            weather_description_list= [(float('-inf'),0,'freezing'),
                                       (0,5,'very cold'),
                                       (5,10,'cold'),
                                       (10,15,'cool'),
                                       (15,20,'pleasant'),
                                       (20,25,'warm'),
                                       (25,30,'hot'),
                                       (30,35,'very hot'),
                                       (35,40,'sweltering'),
                                       (40,float('inf'),'heatwave')
                                       ]
            weather_description= next(desc for low,high,desc in weather_description_list if low<=temperature_value<high)
            weather_report= f' The weather is {temperature_value} degree celsius, which is considered {weather_description}.'

            
            time_report= datetime.datetime.now().strftime('It\'s %A ,%B %d, %Y, The time is %I %M %p in your area,')



            self.report= 'Good '+greeting_phrase+' sir. '+ time_report+weather_report




if __name__=='__main__':
    obj= start_my_day()
    print(obj.report)
    speak(obj.report)
