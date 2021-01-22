import os
from time import time
from random import randrange
from time import sleep
import os
from threading import Thread


last_random = 0

def change_picture(adress):
    os.system('''dbus-send --session --dest=org.kde.plasmashell --type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript 'string: var Desktops = desktops(); d = Desktops[1]; d.wallpaperPlugin = "org.kde.image"; d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General"); d.writeConfig("Image", "''' +  adress + '"' + ");'")

def smart_random(_list_):
    global last_random
    result = randrange(len(_list_))
    while result == last_random:
            result = randrange(len(_list_))
    last_random = result
    return _list_[result]

# random_lsit = []

# def more_smart_random(_list_):


def file_search(cwd):
        try:
                results = [str(i)[ str(i).index("'")  + 1 : -2 ] for i in os.scandir(cwd)]
        except:
                print("An error occured")
                return []

        files = [ [], [] ]

        for i in results:
                if os.path.isfile(cwd) == False and cwd.endswith("/") == False:
                        if os.path.isdir(cwd + "/" + i):
                                files[0].append(i)
                        else:
                                files[1].append(i)
                else:
                        if os.path.isdir(cwd + "/" + i):
                                files[0].append(i)
                        else:
                                files[1].append(i)
        return files


program_state = True


pictures_array = []

time_delay = 60 # set default time of delay

for file in file_search(os.getcwd() + '/pictures')[1]:
        if file.endswith('png') or file.endswith('jpg'):
                pictures_array.append(os.getcwd() + '/pictures/' + file)

def main():
    global program_state
    while program_state:
            sleep(time_delay)
            change_picture(smart_random(pictures_array))
    print("exit...")

def branch():
    global program_state
    global time_delay
    while program_state:
        comand = input()
        if comand == 'exit':
                program_state = False
                print(f'Please stick around for {time_delay} s')
        elif comand.startswith('delay'):
                comand = comand[6 : ]
                if comand.startswith('set'):
                        try:
                                time_delay = int(comand[4 : ])
                                print('Please wait for the loop to restart')
                        except Exception as e:
                                print(str(e))
                elif comand == 'get':
                        print(f'Changed the delay value to {time_delay} s')
        elif comand == 'pictures':
                print(pictures_array)
        else:
                print("Eh?") # imma steal the erlang shell real quick kthx :>


main_thread = Thread(target=main, args=())
branch_thread = Thread(target=branch, args=())
# i created threads for main function and for comands branch


main_thread.start()
branch_thread.start()
# i runnned main thread and kill him when he complete his work

main_thread.join()
branch_thread.join()
# i runnned command branch thread and kill him when he complete his work
