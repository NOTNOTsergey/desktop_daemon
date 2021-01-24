from time import time
from random import randrange
from time import sleep
import os
from threading import Thread


last_random = 0

def change_picture(adress):
    os.system('''dbus-send --session --dest=org.kde.plasmashell --type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript 'string: var Desktops = desktops(); d = Desktops[1]; d.wallpaperPlugin = "org.kde.image"; d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General"); d.writeConfig("Image", "''' +  adress + '"' + ");'")

def smart_random(_list_):
    if _list_ != []:
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
        except Exception as e:
                print("it's an error", e)
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

time_delay = 5 # set default time of delay

for file in file_search(os.getcwd() + '/pictures')[1]:
        if file.endswith('png') or file.endswith('jpg'):
                pictures_array.append(os.getcwd() + '/pictures/' + file)

change_picture(smart_random(pictures_array))

def main():
    global time_delay
    global program_state
    time_last = int(time())
    while program_state:
            if int(time()) - time_last == time_delay:
                time_last = int(time())
                change_picture(smart_random(pictures_array))
    print("main thread off...")

def branch():
    global program_state
    global time_delay
    global pictures_array

    while program_state:
        comand = input()
        if comand == 'exit':
                program_state = False
                print(f'please delay for cycle end {time_delay} s')
        elif comand == 'help':
                print('delay')
                print('    set { number } // set delay in number seconds')
                print('    get // show delay in seconds')
                print('pictures // show pictures in mechanism')
                print('    add { adress of your picture // add picture to random  mechanism')
                print('    remove picture from random mechanism')
        elif comand.startswith('delay'):
                comand = comand[6 : ]
                if comand.startswith('set'):
                        try:
                                time_delay = int(comand[4 : ])
                                print('delay  for reset the main thread')
                        except Exception as e:
                                print(str(e))
                elif comand == 'get':
                        print(f'now delay is {time_delay} s')
        elif comand.startswith('redef'):
                old_pictures_array = pictures_array
                try:
                        for file in file_search(comand[6 : ])[1]:
                                if file.endswith('png') or file.endswith('jpg'):
                                        pictures_array.append(comand[6 : ] + '/' + file)
                except Exception as e:
                        print('an error...')
                        print('! files restored')
                        pictures_array = old_pictures_array
        elif comand.startswith('dir'):
                comand = comand[4 : ]
                if comand.startswith('add'):
                        old_pictures_array = pictures_array
                        try:
                                for file in file_search(comand[4 : ])[1]:
                                        if file.endswith('png') or file.endswith('jpg'):
                                                pictures_array.append(comand[4 : ] + '/' + file)
                        except Exception as e:
                                print('an error...')
                elif comand.startswith('remove'):
                        try:
                                for file in file_search(comand[7 : ])[1]:
                                        if file.endswith('png') or file.endswith('jpg') and file in pictures_array:
                                                pictures_array.remove(comand[7 : ] + '/' + file)
                        except Exception as e:
                                print('an error...')
        elif comand.startswith('pictures'):
                if comand == 'pictures':
                        print(pictures_array)
                else:
                        comand = comand[9 : ]
                        if comand.startswith('add'):
                                if os.path.isfile(comand[4 : ]) and (comand[4 : ].endswith('.jpg') or comand[4 : ].endswith('.png')):
                                        pictures_array.append(comand[4 : ])
                                        print('picture added')
                                else:
                                        print('it is not file, try again')
                        elif comand.startswith('remove'):
                                if comand[7 : ].isnumeric():
                                        pictures_array.remove(pictures_array[int(comand[7 : ]) + 1])
                                else:
                                        pictures_array.remove(comand[7 : ])
                
                
        else:
                print("i can't understand you")


main_thread = Thread(target=main, args=())
branch_thread = Thread(target=branch, args=())
# i created threads for main function and for comands branch


main_thread.start()
branch_thread.start()
# i runnned main thread and kill him when he complete his work

main_thread.join()
branch_thread.join()
# i runnned command branch thread and kill him when he complete his work
