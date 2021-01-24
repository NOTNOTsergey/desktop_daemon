import os
from time import time
from random import randrange
from time import sleep
import os
from threading import Thread


def file_search(cwd):
		try:
			results = [str(i)[ str(i).index("'")  + 1 : -2 ] for i in os.scandir(cwd)]
		except:
			print("it's an error")
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


cwd = os.getcwd()

print(f'i will work in --> {cwd} | directory')
print('check the settings file...')

if 'settings.txt' in file_search(cwd)[1]:
        print('! file founded')
else:
        print('! file not found')
        print('completition work...')
        exit()

f = open(cwd + '/settings.txt')
content = []

for row in f: 
        content.append(row)
f.close()

print(f'main file will work in -> {content[0][16 : ]} | directory')
os.system('cd ' + content[0][16 : ])
print('    >    program control konsole    <    ')
os.system('python -u ' + cwd + '/pic_change_main.py')