password=None
while password !="n":
     password=input("Would you like to roll the About page? y/n?")
     if password !="n":
          print("1597 Ver 1.5 Code Written By Ryland.B of Mailbox CE. Hex Is free Code Not Owned By Mailbox. Paint runner Is from Turtle Demo. Guess The Password Owned By Mailbox")
print("Loading next")
password=None
while password !="n":
     password=input("Would you like To Launch Paint Runner?")
     if password !="n":
          from turtle import *

          def switchupdown(x=0, y=0):
              if pen()["pendown"]:
                  end_fill()
                  up()
              else:
                  down()
                  begin_fill()

          def changecolor(x=0, y=0):
              global colors
              colors = colors[1:]+colors[:1]
              color(colors[0])

          def main():
              global colors
              shape("circle")
              resizemode("user")
              shapesize(.5)
              width(3)
              colors=["red", "green", "blue", "yellow"]
              color(colors[0])
              switchupdown()
              onscreenclick(goto,1)
              onscreenclick(changecolor,2)
              onscreenclick(switchupdown,3)
              return "EVENTLOOP"

          if __name__ == "__main__":
              msg = main()
              print(msg)
print("Loading Next")
password=None
while password !="y":
     password=input("Would You Like To Load The 2 minute Countdown")
     if password !="y":
          import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time_sec -= 1

    print("stop")

countdown(100)

print("Loading Next")
password=None
while password !="n":
     password=input("Would you Like to Load GTSP Free Trail")
     if password !="n":
          print("GTSP By Mailbox CE.Free Trail Edition.Ideas By Carson, Tested By Liam And Josh And Additional Support By Dawson And Rilly")
          print("First Subject:Liv Avice")
          password=None
          while password !="myPassword1234":
                  password=input("Enter to crack")
                  if password !="myPassword1234":
                          print("You got it WRONG!!!")
          print("Congrats,Wait for the full version to come out")
print("Loading Next")
password=None
while password !="y":
     password=input("Would you like to load GTP? y/n")
     if password !="y":
         print("Loading Last")
print("Please Note: You will have to enter product key every startup. Your product key is found in the case")
while password !="801AB74":
    password=input("Please Enter Product Key To Prompt Startup")
    if password != "801AB74":
        print("invalid Product Key")
print("Valid Product Key.")
print("My name is User 4111 and i need YOU to guess my password!!")
print("Welcome to Guesss The Password Ver 2.4.1. Game code by Ryland Bencharski of MAILbox Computer Entertanment")
print("If you would like to support Ukraine during this time go to https://manitoba4ukraine.ca/ to donate")
print("This Is The School Supplies Edition")
password=None
while password !="Pencil":
    password=input("Hello kind sir. Can you please guess my password>>>")
    if password  !="Pencil":
        print("Thats not it. Sorry")
print("Thank you, Thank you.")
password=None
while password !="Eraser":
    password=input("Can you do it again")
if password !="Eraser":
        print("Try again")
print("YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
password=None
while password !="Ruler":
    password=input("Again")
    if password !="Ruler":
        print("k")
print("Yo. Your good ")
password=None
while password !="Binder":
    password=input("A couple more times intil we are done")
    if password !="Binder":
        print("i will give you a hint. it is something you put work in")
print("more")
password=None
while password !="Disc":
    password=input("")
    if password !="Disc":
        print("YOU CAN DO IT!!!!!!!! GUESS AGAIN")
print("YOU DID IT,ACOUPLE MORE!!!")
password=None
while password !="TwoMorePlease":
    password=input("This is it")
    if password !="TwoMorePlease":
        print("I can tell you a hint, You can never guess it!!")
print("Almost Done")
password=None
while password !="MORE":
    password=input("Last one!!")
    if password !="MORE":
        print("NOPE")
print("good")
password=None
while password !="y":
     password=input("Would you like to load the HEX? y/n")
     if password !="y":
          print("Thank You For Using 1597 1.0 if you like the software please feel free to rate it")
from turtle import*
for i in range(72):
    for j in range(6):
            forward(70)
            right(60)
    right(5)
