import time
seconds=0
minutes=0
hours=0
for i in range(86400):
    seconds+=1
    if seconds == 60:
        minutes+=1
        seconds=0
    if minutes == 60:
        hours+=1
        minutes=0
    time.sleep(1)
    print(str(hours).zfill(2),":",str(minutes).zfill(2),":",str(seconds).zfill(2))
