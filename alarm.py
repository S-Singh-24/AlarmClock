import datetime
from playsound import playsound
hour = int(input("Hours: "))
min = int(input("Minutes: "))
amPm = input("AM/PM? ")

if amPm == "pm":
    hour += 12

while True:
    if hour == datetime.datetime.now().hour and min == datetime.datetime.now().minute:
        print("Alarm..")
        playsound("alarm.wav")
        break
