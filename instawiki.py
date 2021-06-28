from instabot import Bot
import os
import wikipedia
y = ("enter subject")
w = wikipedia.summary(y,sentences=10)
c = os.system('rmdir /s config')#for windows
b = input("enter your user name")
a = input("enter your password")
t = input("enter name of reciver")
bot = Bot()
bot.login(username=b,password=a)
bot.send_message(w,[t])
