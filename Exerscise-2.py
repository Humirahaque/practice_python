import time
t = time.strftime('%H:''%M:''%S:')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour:"))
a = input("Enter your name:")



if(hour>=5 and hour<12):
    print("Good Morning",a)
elif(hour>=12 and hour<=17):
    print("Dood Evening",a)
elif(hour>17 and hour<=19):
    print("Good afternoon",a)
else:
    print("Good Night",a)