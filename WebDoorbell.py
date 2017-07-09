import RPi.GPIO as GPIO
import time
import telegram
import os

bot = telegram.Bot(token='PASTE BOT TOKEN HERE')



GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	input_state = GPIO.input(18)
	if input_state == False:
		print("Button Pressed")
		os.system("fswebcam test.jpg")
		time.sleep(0.5)
		bot.send_message(chat_id=PlaceChatIdHere, text="Your doorbell rang")
		bot.send_photo(chat_id=PlaceChatIdHere, photo=open('test.jpg', 'rb'))
		time.sleep(0.5)
		os.system("rm test.jpg")
		time.sleep(0.2)
