import time

t = 10

while t > 0:
    time.sleep(1)
    print(t)
    t -= 1


t = 0

while True:
    time.sleep(1)
    print(t)
    t += 1
