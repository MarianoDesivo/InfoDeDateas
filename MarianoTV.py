import os
import random
from subprocess import Popen
import traceback
import re
import time
import msvcrt
import sys


flag = 0 #Flag to finish this program

#This function is used to close the program by pressing Enter on the console window
def readInput( caption, default, timeout = 5): 

    start_time = time.time()
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13: # enter_key
                input = '1'
                break
            elif ord(byte_arr) >= 32: #space_char
                input += "".join(map(chr,byte_arr))
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break

    if len(input) > 0:
        return input
    else:
        return default

	
try:
        ruta = os.path.dirname(os.path.abspath(__file__)) #Path will be wherever you put MarianoTV.py
        vlc = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" #Path of VLC.exe
        os.chdir(ruta) #Change current working directory to the folder which has MarianoTV.py
        archivos=[] #List to append filenames 
        vistos =[]  #List to append filenames of videos you have already whatched
        vistostxt = [] #List for writing a txt with the list of watched videos


        for folder, subfolders, files in os.walk(ruta): #walk through the folder and all subfolders looking for videos
                for file in files:
                        if file != ruta + '\\' + 'CapitulosVistos.txt': #not to open the .txt file
                                archivos.append(folder + '\\' + file) #Add path and name of the file
        

        f = open('CapitulosVistos.txt', 'a') #Create (if it does not exist) the file that will list every video we have watched
        f.close() 
        
        f = open('CapitulosVistos.txt') #Open to read txt                      
        vistos = f.readlines()          #Create a list with the files on the .txt
        f.close() 
                        
       

        

        if len(vistos) == 0: #If we haven't watched any video
                vistos.append('1') #Set the counter to 1

        for i in range(len(vistos)):
                vistos[i] = vistos[i].replace('\n','') 
                
        contador = int(vistos[0]) #Read the counter, convert it to int
        print(contador, 'contador inicial')
                

        while True:
                video = random.choice(archivos) #Randomly chooses a video from the list
                if video in vistos:
                        print('Ya viste ' + video)
                        if random.randint(1,10) == 1: #There is a 10% chance to watch a video you have already seen
                                print('pero lo vemos igual')
                                subprocess.run([vlc,'--play-and-exit','-f', video], shell=True)
                                
                                contador+=1
                else:
                        if not (('.txt' or '.py') in video):
                                contador += 1 

                                if contador > 300: #If we have watched more than 300 videos 
                                        f = open('CapitulosVistos.txt', 'w')    #Reset the list to start again
                                        f.close()
                                        print(contador,vistos[0])
                                        vistos=[]
                                        vistos.append('0')
                                        contador=0
                                        continue 
                                
                                vistos[0] = str(contador) #Update counter

                                vistos.append(video) #Add the video you just watched to the list
                                vistostxt = vistos
                                for i in range(len(vistostxt)):
                                        if not vistostxt[i].endswith('\n'): 
                                                vistostxt[i] = vistostxt[i] + '\n' #Each element is separated by \n (not csv)
                        
                                f = open('CapitulosVistos.txt', 'w') 
                                f.writelines(vistostxt) #Write again txt register
                                print('-------------------reescribo:', vistostxt)
                                f.close()
                                        
                                
                                print('reproduciendo',video)

                                process = Popen([vlc,'--play-and-exit','-f', video]) #Open video in background with Popen
                                print('Enter para salir...') #Press enter to exit...
                                while process.poll() is None: #While video is playing
                                        flag = readInput('Enter para salir...', False, 1) #Wait 1 second for you to press Enter, if not repeat                                       
                                        if flag:
                                                break
                                if flag:
                                        break
                                

except:
        f.close() #In case of an error close .txt
        print('f.close()')
        traceback.print_exc() 
        time.sleep(120) #2 minutes to read the error message
        
                
