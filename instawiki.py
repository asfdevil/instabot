from instabot import Bot
import os
import wikipedia
w = wikipedia.summary("about",sentences=10)
c = os.system('rmdir /s config')
b = input("enter your user name")
a = input("enter your password")
t = input("enter name of reciver")
bot = Bot()
bot.login(username=b,password=a)
bot.send_message(w,[t])
