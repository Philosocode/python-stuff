import threading
import time
print("Start!")


def takeNap():
    time.sleep(10)
    print("Wake up!")


threadObj = threading.Thread(target=takeNap)
threadObj.start()

print("End!")
