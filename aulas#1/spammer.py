import pyautogui as spam
import time

limite_msg = input('enter n de mensagens: ')
msg = input('coloque a msg: ')

i = 0

time.sleep(2)

while i<int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")

i+=1