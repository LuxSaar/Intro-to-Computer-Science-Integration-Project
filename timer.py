#Lucas Eusebio Veras
#As of now it is quite literally just a timer, but hopefully I should be able to save values to make it into a time management program
#Works cited
#https://realpython.com/python-sleep/
#https://www.saltycrane.com/blog/2011/11/how-get-username-home-directory-and-hostname-python/
import time
import getpass
userName = getpass.getuser()
#assigns the username of the user as a variable.
print("Hello",userName,"Welcome to timer app (name pending)",sep="_", end=".\n")
#This next section is basically just gonna be dumping all of the numeric/string operators
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

time.sleep(1)
#tells the program to wait one second before prompting the user
while 0 == 0: 
    timer_length0 = input("Set a timer (microwave format): ")
    if timer_length0.isnumeric() == False:
        print("invalid input")
    else:
        timer_length = int(timer_length0)
        if (timer_length%100)!=0:
            if 59 <(timer_length-(timer_length-(timer_length%100))):
                print("invalid input")
            else:
                while timer_length > (0):
                    time.sleep(1)
                    if timer_length%100 !=0 or timer_length == 1:
                        timer_length-=1
                    else:
                        if timer_length != 0:
                            timer_length-=41
                    print(timer_length)
                    if timer_length == 0:
                        pass
