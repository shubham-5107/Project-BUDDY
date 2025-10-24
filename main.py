import pyttsx3, speech_recognition as sr
import time, webbrowser, os,subprocess


class gods:

    def __init__(self,cache_file,org_file=None):
        self.org_file=org_file
        self.cache_file= cache_file

    def vishnu(self):
        with open(f'BACKEND/{self.org_file}.py') as f:
            data= f.read()

        with open(f'{self.cache_file}.py','w') as f:
            f.write(data)

    def shiva(self):
        os.remove(f'{self.cache_file}.py')

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
        return 'None'
    return query

def processor(query):
    print('admin:', query)
    
    match query:
        case 'None':
            return '\n'

        case s if 'go to sleep' ==s or 'you may rest now buddy' == s:
            quit()
        
        case h if 'hello' in query.split():
            return 'hello shubham sir'
  
        case 'start my day':
            gods('cache_start_my_day','start_my_day').vishnu()
            import cache_start_my_day as smd
            report= smd.start_my_day().report
            
            try:
                gods('cache_start_my_day').shiva()
            except Exception as e:
                print(e)
            return report
            
        case s if 'website' in s.split() and 'Chrome' in s.split():
            root_domain= query.split('website')[-1].split('on')[0].replace(' ','')
            print(f'opening website {root_domain}.com on Chrome...')
            webbrowser.open(f'www.{root_domain}.com')
            return ''

        case s if 'set' in s.split() and 'timer' in s.split() or 'start' in s.split() and 'timer' in s.split():
            speak('timer started')
            gods('cache_timer','timer').vishnu()

            def paraphraser(query):
                l1=[]

                for i in query.split():
                    if i.isdigit():
                        l1.append(i)
                l2=len(l1)

                l=[]
                if l2==3:
                    for i in query.split():
                        try:
                            l.append(str(int(i)))
                        except Exception as e:
                            pass
                
                elif l2==2:
                    for i in range(len(query.split())):
                        # print(query.split()[i])
                        if query.split()[i]=='hours':
                            l.append(query.split()[i-1])
                            for j in range(len(query.split())):
                                if query.split()[j]=='minutes':
                                    l.append(query.split()[j-1])
                                    break

                                elif query.split()[j]=='seconds':
                                    l.append(f'0,{query.split()[j-1]}')
                                    break
                            break
                        
                        elif query.split()[i]=='minutes':
                            l.append(f'0,{query.split()[i-1]}')
                            for j in range(len(query.split())):
                                if query.split()[j] == 'seconds':
                                    l.append(query.split()[j-1])
                                    break
                            break
                        
                        elif query.split()[i]=='seconds':
                            l.append(f'0,0,{query.split()[i-1]}')
                            break
                elif l2==1:
                    for i in range(len(query.split())):
                        if query.split()[i] == 'hours':
                            l.append(query.split()[i-1])
                            break
                        elif query.split()[i] == 'minutes':
                            l.append(f'0,{query.split()[i-1]}')
                            break
                        elif query.split()[i] == 'seconds':
                            l.append(f'0,0,{query.split()[i-1]}')
                            break

                return ','.join(l)+')'+'\n'

            with open('cache_timer.py','a') as f:
                f.write(paraphraser(query))
            
            subprocess.Popen(['python','cache_timer.py'])
            time.sleep(.1)

            try:
                gods('cache_timer').shiva()
            except Exception as e:
                pass
            return ''
        
        case s if 'what' in query.split() and 'is' in query.split():
            if query.split()[2].isdigit() and query.split()[-1].isdigit():
                if query.split()[3] =='+':
                    answer= int(query.split()[2]) + int(query.split()[-1])
                elif query.split()[3] =='-':
                    answer= int(query.split()[2]) - int(query.split()[-1])
                elif query.split()[3] =='*':
                    answer= int(query.split()[2]) * int(query.split()[-1])
                elif query.split()[4]== 'divided':
                    answer= int(query.split()[2]) / int(query.split()[-1])
                
                return str(answer)
                
        case s if query.split()[0]=='add':
            return query.split()[1] + query.split()[-1]
        case s if query.split()[0]=='subtract':
            return query.split()[1] - query.split()[-1]
        case s if query.split()[0]=='multiply':
            return query.split()[1] * query.split()[-1]
        case s if query.split()[0]=='divide':
            return query.split()[-1] / query.split()[1]

    return 'Sorry sir I can\'t do it, I can assist you with something else, please let me know'

if __name__=='__main__':
    while True:
        answer= processor(take_command())
        print(answer)
        speak(answer)
    