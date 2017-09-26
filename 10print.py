from random import uniform
from time import sleep
from sys import stdout

prob = 0.1

while True:
    if uniform(0, 1) < prob:
        stdout.write('/')
    else:
        stdout.write('\\')
    stdout.flush()
    sleep(0.1)
