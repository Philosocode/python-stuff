""" python3
stopwatch.py - Simple stopwatch program
"""

import time

# Display instructions
print("""Press ENTER to begin. After, press ENTER to 'click' the stopwatch.
      Press Ctrl-C to quit.""")
input()
print("Started")
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end="")
        lapNum += 1
        lastTime = time.time()  # Reset last lap time
except KeyboardInterrupt:
    # Handle C-c exception
    print('\nDone')
