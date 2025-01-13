import datetime
datetime = input("What time is it?: ")
morning = "Time to wake up!"
afternoon = "Time to go outside"
evening = "We can play games now" if datetime == "18:00" else "We can't play game until 18:00"
print (evening) if datetime < "06:00" >= "12:01" else "Check the time" 

#Determine if morning
morning if datetime == "06:00" or datetime > "11:00" else "its not time to wake up"
print(morning)
afternoon = "Time to go outside"
