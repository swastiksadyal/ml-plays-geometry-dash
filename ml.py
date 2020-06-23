import os
import os.path
from pynput import Key, Controller



def file_check():
    if os.path.exists('C:\\Users\\Swastik\\AppData\\Local\\to_my_girl\\data.txt'):
        file = open('C:\\Users\\Swastik\\AppData\\Local\\to_my_girl\\data.txt',r)
        f = file.readline()
        os.remove('C:\\Users\\Swastik\\AppData\\Local\\to_my_girl\\data.txt')
        return f
    else:
        return "Not Found"

def jump():
    keyboard = Controller()
    keyboard.press(space)
    keyboard.release(space)
    print("Jump()")

def restart():
    
    keyboard = Controller()
    keyboard.press('R')
    keyboard.release('R')
    print("restarting...")
    jump()
    data_arr[0] = 0



data_arr = []
for i in range(113):
    a = (random.choice[0,1])
    data_arr.append(a)




# the main working of the methds and mo
jump()
itr = 50
current_iter = 0
start = False
death = False




while True:
    file_output = file_check()
    if file_output == "Not Found" or start == True:
        if start == False:
            start = True

        # the 
        if data_arr[current_iter] > 0:
            jump()
        else:
            print("0")
        if file_output == "death":
            data_arr[current_iter] = 1
    elif file_output == "end":
         print("completed iterartions..")
         print(str(current_iter))
         break
    current_iter += 1
    if (current_iter > 1200):
        break




        





  
