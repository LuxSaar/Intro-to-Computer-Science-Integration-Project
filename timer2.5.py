import time
from datetime import datetime

print("Hello User", "Welcome to Lux's Activity Tracker",
      sep="_", end=".\n")
time.sleep(1)


def dotimer(tlength):
      '''literally just the timer'''
    while tlength > 0:
        print(tlength)
        time.sleep(1)
        if tlength % 100 != 0 or tlength == 1:
            tlength -= 1
        else:
            if tlength != 0:
                tlength -= 41
        if tlength == 0:
            pass


def initiate_timer():
      '''starts the timer depending on the number input'''
    timer_length0 = input("Set a timer (microwave format): ")
    if not timer_length0.isnumeric():
        print("invalid input")
    else:
        timer_length = int(timer_length0)
        if (timer_length % 100) != 0:
            timer_length1 = int(timer_length0)
            dotimer(timer_length)
        elif (timer_length % 100) == 0:
            timer_length1 = int((timer_length / 100) * 60)
            dotimer(timer_length)
        else:
            timer_length1 = None
        return timer_length1


def initiate_stopwatch():
      '''starts the stopwatch'''
    input("Press Enter to start")
    start_time = time.time()
    input("Press Enter to stop")
    end_time = time.time()
    time_passed = end_time - start_time
    return time_passed


def activity_tracker(activity):
      '''actually tracks the amount of time spent on the activity, however record is what writes it into the file, also asks for preference between timer and stopwatch'''
    print("Input 1 for Timer")
    print("Input 2 for Stopwatch (does not display current time)")
    timer_or_stopwatch = input()
    if not timer_or_stopwatch.isnumeric():
        print("Invalid Input")
    elif int(timer_or_stopwatch) == 1:
        timer_length = initiate_timer()
        if timer_length == None:
            pass
        else:
            valuethingy = round((int(timer_length)) / 60)
            if round(int(timer_length)) <= 59:
                  valuethingy = round(int(timer_length))
                  print("You have completed a",
                        int(round(int(timer_length))),
                        "second session of", activity + "!")
                  return int(valuethingy), "seconds of", activity
            else:
                  print("You have completed a",
                        int(round(int(timer_length)) / 60),
                        "minute session of", activity + "!")
                  return int(valuethingy), "minutes of", activity
    elif int(timer_or_stopwatch) == 2:
        stopwatch_length = initiate_stopwatch()
        valuethingy = round((int(stopwatch_length)) / 60)
        if round(int(stopwatch_length)) <= 59:
            valuethingy = round(int(stopwatch_length))
            print("You have completed a",
                  int(round(int(stopwatch_length))),
                  "second session of", activity + "!")
            return int(valuethingy), "seconds of", activity
        else:
            print("You have completed a",
                  int(round(int(stopwatch_length)) / 60),
                  "minute session of", activity + "!")
            return int(valuethingy), "minutes of", activity
    else:
        print("invalid input")


def record_activity(activity_iq):
      '''records the activities'''
    date = str(datetime.date(datetime.now()))
    record_file = open(date + ".txt", 'a')
    record_file.write(str(activity_iq))
    record_file.write("\n")


def main():
      '''the main function, basically just the start menu and the way to exit the program'''
    sactivity = None
    while sactivity != "EP":
        input("Press Enter to record an activity")
        sactivity = input("What activity would you like to do? (Input EP to exit the program)")
        if sactivity == "EP":
            pass
        else:
            activity1 = activity_tracker(sactivity)
            record_activity(activity1)

main()
# Okay to make this as brief as possible, I understand that there are a ton of things I could have done to facilitate this including but not limited to using
# The time conversion function, as well as a more intuitive way to exit the program and menu. I'm going to continue working on this after the class is over
# As of now all it does is record time spent doing an activity, and it cannot gather the data, but I will be making it do that in the future. 
# Here I'm going to be writing all of the requirements I missed in the program above, and they should show up as soon as you choose to exit the program.
print(10**2)
#prints 100 (exponential operator) 10^2
print(10*2)
#prints 20 (multiplication 10 times 2)
print(10/2)
#prints 5 (10 divided by 2)
print(10%3)
#I already have something with a modulus operator, but this comes out as 1 since it spits out the remainder of a division function
print(10//3)
#prints 3 (division but it discards the remainder)
print(10+2)
#pretty self explanatory, prints 12 (addition)
print(10-2)
#again self explanatory, prints 8 (subtraction)
print("hello"*10)
#prints hello 10 times with no spaces, basically just repeats the string
print("hello"+"goodbye")
#prints hello and goodbye with no spaces.
testvar = 5
bestvar = 6
lestvar = 7
if testvar == 5 or lestvar == 8 or bestvar == 7:
    print("at least one of them is the value being checked for")
#basically checks if either testvar is 5, lestvar is 8, and bestvar is 7, since at least one of them is true it prints the statement.
testvar = 5
if testvar == 5 and lestvar == 8 and bestvar == 7:
    print("all of the variables are the values being checked for")
#basically the same thing as or, but instead of only one of them having to be true, all of them have to be
print(not testvar == 5)
#inverts the true/false value of any particular statement, here since testvar is equal to 5, it prints false, if testvar was say equal to 6 it would print True instead
mestvar = 1
for mestvar in range(1,6):
        print(mestvar)
#for loop that prints the numbers 1-5
#If anything is missing check the first timer.py version also included.
