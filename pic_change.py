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


cwd = os.getcwd()

print(f'Working dir: {cwd}')
print('Checking the settings file...')

if 'settings.txt' in file_search(cwd)[1]:
        print('! found')
else:
        print('! file not found')
        print('Exiting')
        exit()

f = open(cwd + '/settings.txt')
content = []

for row in f: 
        content.append(row)
f.close()

print(f'The main file is going to run in {content[0][16 : ]}')
os.system('cd ' + content[0][16 : ])
print('    >    INITIATING THE CONTROL CENTER    <    ')
os.system('python -u ' + cwd + '/pic_change_main.py')
