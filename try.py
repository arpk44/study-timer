#List of all Imports

import random
import time 
from time import sleep
from winsound import PlaySound
import winsound

# ALL FUNCTIONS GO BELOW HERE

#Page Seperator

def page_sep():
    print("-----------------------------------------------------------------------------------")

# Play Music Function

def playmusic():
    # 1000 hz is frequency
    freq = 1000
 
    # duration is set to 100 mms          
    dur = 100
    # play music
    winsound.PlaySound('eminem.wav', 0) # Plays the Eminem Song

    print("Times Up!!")

    # Last Few Beeps

    i = 1 # establish i
    while i < 14:
     winsound.Beep(freq, dur)
     i+= 1

#Function - 5 Second Last Timer

def last_timer():
    print("5")
    sleep(1)
    print("4")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("0")

#basic 1 min timer for other uses
def one_min():
    print("Running a 1 minute timer")
    sleep(1)
    print("00:01:00 starts now...")
    
    sleep(55) # Code stops for 55 seconds; it reruns and counts down in the next line

    last_timer() # uses the function and runs a lot of code

    playmusic()

    # End of the 1 minute Timer Code
    page_sep()

# Function for Time Listing
def list_times():
    print("Select the amount of minutes you would like the timer to be set. Note hours must be written in minutes.")
    # Options for Times
    print("1 minute | 2 minutes | 10 minutes | 35 minutes | 45 minutes | Custom")
    sleep(2)
    print("For custom, just enter the digit. [For Example: 60 minutes would be 60!")

# Five Min Timer

def five_min():
    print("Running a 5 minute timer")
    sleep(1)
    print("00:05:00 starts now...")
    
    sleep(295) # Code stops for 55 seconds; it reruns and counts down in the next line

    last_timer() # uses the function and runs a lot of code

    playmusic()

    # End of the 1 minute Timer Code
    page_sep()

# ALL MAIN CODE GOES BELOW THIS


# Program Welcome

page_sep()
print("Hellooooo")
print("I am your study timer. Welcome!! ")
print()
page_sep()

# Enter Name

name = input("What is your name? ")

page_sep()

# Time Listing

list_times()

# Work on The Main Part (timer)

input_user = input(("Which time?? Type Number ONLY [for example: 1]: "))
user_time = int(input_user)
page_sep()
# Running the user_time

if user_time == 1:
    one_min()
    print("Finished", name)
    #code stops
    print("Congragulations. This was a short timer, so no break will be given. Good job, though! Keep the good work up :)")
elif user_time == 2:
    sleep(2)
    print("Running a 2 minute timer")
    sleep(1)
    print("00:02:00 starts now...")
    
    sleep(115) # Code stops for 55 seconds; it reruns and counts down in the next line

    last_timer() # uses the function and runs a lot of code

    playmusic()

    # End of the 2 minute Timer Code
    page_sep()
    print("Finished", name)
    print("This was great. Good job! Hope you got lots done <3. No break will be given because the timer was short. ")
    #code stops
elif user_time == 10:
    sleep(2)
    print("Running a 10 minute timer")
    sleep(1)
    print("00:10:00 starts now...")
    prod = user_time * 60
    prod = prod - 5
    sleep(prod) # Code stops for ## seconds; it reruns and counts down in the next line

    last_timer() # uses the function and runs a lot of code

    playmusic() #plays music

    # End of the 10 minute Timer Code
    page_sep()
    print("Finished", name)
    print("Great job, ", name, " proud of you. You will be given a 1 minute break. Hope you did lots of work!!")
    
    sleep(2)
    print("Timer starts now. Be prepared")

    one_min()

    #code stops 
else:
    sleep(2)
    print("Running a 10 minute timer")
    sleep(1)
    print("00:10:00 starts now...")
    prod = user_time * 60
    prod = prod - 5
    sleep(prod) # Code stops for ## seconds; it reruns and counts down in the next line

    last_timer() # uses the function and runs a lot of code

    playmusic() # plays the music

    # End of the 10 minute Timer Code
    page_sep()
    print("Finished", name)
    print("Great job, ", name, " proud of you. You will be given a 5 minute break. Hope you did lots of work!!")
    
    sleep(2)
    print("Timer starts now. Be prepared")

    five_min()

    print("Done. Good job!")

# End Page

page_sep()

print("Reflection/Feedback")
 
# Reflection

subject = input("What did you study? ")
reflection = input("In a scale of 1-10. How was the study session? [1 = bad, 10 = best] ")

print(subject)
print(reflection)

# Sum Up 

page_sep()

print(name, " studied for ", user_time, " minutes. They studied the subjects/topics ", subject, ".") # prints final reflection

# Thanks for using :)
