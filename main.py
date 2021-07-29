import pyautogui as pt
from time import sleep
import pyperclip
import random
import pandas as pd


sleep(3)


df = pd.read_excel('C:/Users/dell/Desktop/whatsapp/TeleNumber.xlsx')
liste= df['numeros'].tolist()


for i in liste:
    def gt_mes(): 
        global x, y

        position = pt.locateOnScreen(r"C:/Users/dell/Desktop/whatsapp/add.png", confidence=.6)
        x = position[0]
        y = position[1]
        pt.moveTo(x + 20, y + 20, duration=.5)
        pt.tripleClick()
    gt_mes()
    def rech_message():
        global x, y

        position = pt.locateOnScreen(r"C:/Users/dell/Desktop/whatsapp/rech.png", confidence=.6)
        x = position[0]
        y = position[1]
        pt.moveTo(x + 60, y + 60, duration=.5)
        pt.tripleClick()
        pt.typewrite(str(i), interval=.01)
    rech_message()
    
    def rech_per():
        global x, y

        position = pt.locateOnScreen(r"C:/Users/dell/Desktop/whatsapp/sh.png", confidence=.6)
        x = position[0]
        y = position[1]
        pt.moveTo(x, y, duration=.05)
        pt.moveTo(x, y + 140, duration=.5)
        pt.click()
    rech_per()


    def post_response():
        global x,y
        position = pt.locateOnScreen(r"C:/Users/dell/Desktop/whatsapp/smile.png", confidence=.6)
        x = position[0]
        y = position[1]
        pt.moveTo(x + 200, y, duration=.5)
        pt.click()
        pt.typewrite("Bonjour, je suis khadija",interval=.01)
        pt.typewrite("\n", interval=.01)
        print(str(i) + "  Done")

    post_response()
    
    def piece():
        global x,y
        position = pt.locateOnScreen(r"C:/Users/dell/Desktop/whatsapp/smile.png", confidence=.6)
        x = position[0]
        y = position[1]
        pt.moveTo(x +60 , y , duration=.5)
        pt.click()
        pt.moveTo(x +60 , y -200 , duration=.5)
        pt.click()
        #pt.moveTo(x +60 , y -710 , duration=.5)
        #pt.click()
        #pt.typewrite("C:/Users/Khadija Bhigh/Desktop/whatsapp")
        pt.moveTo(x +60 , y -280 , duration=.5)
        pt.click()
        pt.typewrite("Doube.csv")
        pt.moveTo(x +350 , y -260 , duration=.5)
        pt.click()
        pt.moveTo(x +680 , y -90 , duration=.5)
        pt.click()
        print(str(i) + "  Done")

    #piece()
    
    def get_message():
        global x, y
        position = pt.locateOnScreen(r"C:/Users/dell/Desktop/whatsapp/smile.png", confidence=.6)
        x = position[0]
        y = position[1]
        pt.moveTo(x + 70, y - 55, duration=.5)
        pt.tripleClick()
        pt.rightClick()
        pt.moveRel(13, 15)
        pt.click()
        whatsapp_message = pyperclip.paste()
        
        
        if pt.pixelMatchesColor(int(x + 70), int(y - 35), (255, 255, 255), tolerance=10):
            print(whatsapp_message)
            df.loc[df['numeros']==i,'reponses']=whatsapp_message
        else:
            print("NoAnswer")
            df.loc[df['numeros']==i,'reponses']="NoAnswer"
            
        #df.to_excel('C:/Users/Khadija Bhigh/Desktop/whatsapp/ReponsesWafa.xlsx')
        
    get_message()
    
    
    def check_for_new_messages():
        pt.moveTo(x + 50, y - 35, duration=.5)

        while True:
            try:
                position = pt.locateOnScreen(r"C:/Users/dell/Desktop/whatsapp/green.png", confidence=.7)

                if position is not None:
                    pt.moveTo(position)
                    pt.moveRel(-100, 0)
                    pt.click()
                    sleep(.5)
            except(Exception):
                print("Aucun reponse")
     
            if pt.pixelMatchesColor(int(x + 50), int(y - 35), (255, 255, 255), tolerance=10):
                print("blanc")
                processed_message = process_response(get_message())
                post_response(processed_message)
            else:
                print("Aucun message")
            sleep(5)
    
    #check_for_new_messages()


    def process_response(message):
        random_no = random.randrange(3)
        if "?" in str(message).lower():
            return "ne me pose pas de questions !"
        else:
            if random_no == 0:
                return "Bienvenue"
            elif random_no == 1:
                return "Merci"
            else:
                return "Au revoir"
            
            
    #processed_message = process_response(get_message())

    







