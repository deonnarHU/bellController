from gpiozero import LED
from time import sleep
from threading import Timer
import time

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)

def func(a, b):
    print("Called function")
    return a * b
 
# Schedule a timer for 5 seconds
# We pass arguments 3 and 4
t = Timer(5.0, func, [3, 4])
 
start_time = time.time()
 
# Start the timer
t.start()
 
end_time = time.time()
 
if end_time - start_time < 5.0:
    print("Timer will wait for sometime before calling the function")
else:
    print("5 seconds already passed. Timer finished calling func()")