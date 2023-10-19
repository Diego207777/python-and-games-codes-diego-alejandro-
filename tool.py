# diego alejandro no delete this line please 


import os 
import colorama

menu_options = {
     
    1: 'Reboot phone ',
    2: ' adb devices ',
    3: ' install adb  Ubuntu ',
    4: 'Exit',
}
# diego alejandro no delete this line please 
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
# diego alejandro no delete this line please 
# diego alejandro no delete this line please 
# diego alejandro no delete this line please 
# diego alejandro no delete this line please 
# diego alejandro no delete this line please 
# diego alejandro no delete this line please 

def option1():
     print(' reboot phone now waiting moment please ....  \'Option 1\'')
     os.system('adb reboot ')
# diego alejandro no delete this line please 
# diego alejandro no delete this line please 
def option2():
     print(' ver dispositivos see  \'Option 2\'')
     os.system('adb devices ')
     print('every the devices  USB')
def option3():
     print(' install adb start \'Option 3\'')
     os.system('apt install adb ')
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            # diego alejandro no delete this line please 
            # diego alejandro no delete this line please 
            # diego alejandro no delete this line please 
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
         
            
            print('good evenning bye by diego alejandro ')
            exit()
        else:
            print(' please select only options in the menu   .')
            # diego alejandro no delete this line please 
            # diego alejandro no delete this line please 
            # diego alejandro no delete this line please 
            print('thanks for use this tool ')
