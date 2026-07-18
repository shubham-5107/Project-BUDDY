import time

class timer:
    def paraphraser(self, query):
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
                        if query.split()[i]=='hours':
                            l.append(query.split()[i-1])
                            for j in range(len(query.split())):
                                if query.split()[j]=='minutes':
                                    l.append(query.split()[j-1])
                                    l.append('0')
                                    break

                                elif query.split()[j]=='seconds':
                                    l.append(0)
                                    l.append(query.split()[j-1])
                                    break
                            break 
                        
                        elif query.split()[i]=='minutes':
                            l.append(0)
                            l.append(query.split()[i-1])
                            for j in range(len(query.split())):
                                if query.split()[j] == 'seconds':
                                    l.append(query.split()[j-1])
                                    break
                            break
                        
                        elif query.split()[i]=='seconds':
                            l.append(0)
                            l.append(0)
                            l.append(query.split()[i-1])
                            break 
                elif l2==1:
                    for i in range(len(query.split())):
                        if query.split()[i] == 'hours':
                            l.append(query.split()[i-1])
                            l.append(0)
                            l.append(0)
                            break
                        elif query.split()[i] == 'minutes':
                            l.append(0)
                            l.append(query.split()[i-1])
                            break
                        elif query.split()[i] == 'seconds':
                            l.append(0)
                            l.append(0)
                            l.append(query.split()[i-1])
                            break
                return l
    
    def buzzer(self, l):
        self.hours= float(l[0])
        self.minutes= float(l[1])
        self.seconds= float(l[2])

        sleep_value= self.hours*3600+ self.minutes*60+self.seconds

        time.sleep(sleep_value)
        print('Timer Ended')
        time.sleep(.1)
        print('Timer Ended')
        time.sleep(.1)
        print('Timer Ended')


if __name__ == "__main__":
    obj= timer()
