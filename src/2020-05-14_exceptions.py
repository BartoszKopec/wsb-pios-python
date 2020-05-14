from datetime import datetime
import sys

class InitializationError(Exception):
   pass

def log(s):
    print(datetime.now().strftime('[%Y-%m-%d %H:%M:%S.%f]'), s)

def importantFunction():
    log('Program initializating variables')
    x=5
    s='0'
    try:
        x/s
    except:
        raise InitializationError('Program could not initialize variables')

log('Checking if program can run')
assert ('win32' in sys.platform), 'This program runs on win32 only. This platform is: ' + sys.platform
log('Program can run')
log('Checking if program can find important file.txt')
try:
    with open('src/file.txt') as file:
        data = file.read()
    log('Program found file.txt')
except FileNotFoundError:
    log('Program could not find file.txt')


#Initialization
try:
    importantFunction()
except InitializationError as e:
    log(e)