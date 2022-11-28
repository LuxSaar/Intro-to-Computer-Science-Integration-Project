import time
import getpass

userName = getpass.getuser()
print("Hello", userName, "Welcome to Lux's Activity Tracker", sep="_", end=".\n")

time.sleep(1)

def initiatetimer():
    timer_length0 = input("Set a timer (microwave format): ")
    if not timer_length0.isnumeric():
        print("invalid input")
    else:
        timer_length = int(timer_length0)
        if (timer_length % 100) != 0:
            timer_length1 = int(timer_length0)
            while timer_length > 0:
                print(timer_length)
                time.sleep(1)
                if timer_length % 100 != 0 or timer_length == 1:
                    timer_length -= 1
                else:
                    if timer_length != 0:
                        timer_length -= 41
                if timer_length == 0:
                    pass
        elif (timer_length % 100) == 0:
            timer_length1 = int((timer_length/100)*60)
            timer_length = int((timer_length/100)*60)
            while timer_length > 0:
                print(timer_length)
                time.sleep(1)
                if timer_length % 100 != 0 or timer_length == 1:
                    timer_length -= 1
                else:
                    if timer_length != 0:
                        timer_length -= 41
                if timer_length == 0:
                    pass
        return timer_length1
def initiatestopwatch():
    input("Press Enter to start")
    starttime = time.time()
    input("Press Enter to stop")
    endtime = time.time()
    timepassed = endtime-starttime
    return timepassed

def activitytracker(activity):
    timerOrStopwatch = input("Send 1 if you'd like to set a designated amount of time for the activity or send 2 if you'd like to time yourself")
    if int(timerOrStopwatch) == 1:
        timerLength = initiatetimer()
        print("You have completed a", int(round(int(timerLength))/60), "minute session of", activity)
        valuethingy = round(int(timerLength))/60
        return int(valuethingy), "minutes of", activity
    elif int(timerOrStopwatch) == 2:
        stopwatchLength = initiatestopwatch()
        print("You have completed a", int(round(int(stopwatchLength))/60), "minute session of", activity)
        valuethingy = round(int(stopwatchLength))/60
        return int(valuethingy), "minutes of", activity
    else:
        print("invalid input")
def main():
    while True:
        input("Press Enter to record an activity")
        Sactivity = input("What activity would you like to do?")
        activity1 = activitytracker(Sactivity)
        #here I'll probably end up recording the activities and this would repeat until the program is terminated
