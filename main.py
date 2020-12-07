from facerec import start_fr
from mms import sendalert
from augustlock import SmartLock
from mot import motion
from soundrl import backdoor,playsound,voicepass

def main():

    while 1==1: 
        mot = motion()       
        
        granted = 0
        if mot == 1:
            playsound("Welcome, please present your face to the camera, subject")
            granted += start_fr()
            print("FR sequence over " + str(granted))
            if granted == 0: 
                bd = backdoor("backdoor password 1")
                if bd == 1: 
                    playsound("please say second password")
                    bd += backdoor("backdoor password 2")
                    if bd == 2: 
                        playsound("please say third password")
                        bd += backdoor("please say third password
                        if bd == 3: 
                            granted = 2
                        else: 
                            granted = 0
                    else: 
                        granted = 0
                else: 
                    granted = 0

            elif granted == 1: 
                c = voicepass("secret password")
                print("voicepass returned" + str(c))
                if c == 1: 
                    granted += 1
            else: 
                continue
            #instantiate smartlock class
            ag = SmartLock()    
            #unlock if both conditions are satisfied
            if granted == 2:
                try:
                    ag.unlock()
                    playsound("Welcome, agent 47")
                except: 
                    playsound("Sorry, unable to open sesame")
            elif granted == 0 or granted == 1:
                try:
                    ag.lock()
                    playsound("You are not authorized to enter, leave the premises immediatly or face termination from this realm of existence")

                except:
                    print("There was an error")
                try:
                    sendalert("Unauthorized entity detected")
                except:
                    continue
            else:
                print("end of loop")
        sleep(120)
        try: 
            ag.lock()
        except: 
            playsound("Door not locked")

if __name__ == "__main__":
    main()
