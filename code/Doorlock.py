from rpi_lcd import LCD
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
card = SimpleMFRC522()
lcd = LCD()
rows = [32,36,38,40]
columns = [31,33,35,37]
relay_pin = 8
buzzer_pin = 10
GPIO.setup(relay_pin,GPIO.OUT)
GPIO.setup(buzzer_pin,GPIO.OUT)
GPIO.output(relay_pin,GPIO.HIGH) # door is lock initially #

for i in rows:
    GPIO.setup(i,GPIO.OUT)
   
for j in columns:   
    GPIO.setup(j,GPIO.IN,pull_up_down = GPIO.PUD_UP)

def keypad():
      lcd.text("Enter the code ",1)
      GPIO.output(rows[0],GPIO.LOW)
      GPIO.output(rows[1],GPIO.HIGH)
      GPIO.output(rows[2],GPIO.HIGH)
      GPIO.output(rows[3],GPIO.HIGH)
      
      if(GPIO.input(columns[0]) == 0):
            lcd.text("open",2)
            GPIO.output(relay_pin,GPIO.LOW) # door unlock #
            GPIO.output(buzzer_pin,GPIO.LOW)
            time.sleep(5)
            GPIO.output(relay_pin,GPIO.HIGH)#door gets lock after 5s #
            
      elif(GPIO.input(columns[1]) == 0):
            lcd.text("Wrong code",2)
            GPIO.output(relay_pin,GPIO.HIGH) # door remains lock #
            GPIO.output(buzzer_pin,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(buzzer_pin,GPIO.LOW)
      elif(GPIO.input(columns[2]) == 0):
            lcd.text("wrong code",2)
            GPIO.output(relay_pin,GPIO.HIGH) # door remains lock #
            GPIO.output(buzzer_pin,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(buzzer_pin,GPIO.LOW)
      elif(GPIO.input(columns[3]) == 0):
            lcd.text("wrong code",2)
            GPIO.output(relay_pin,GPIO.HIGH)
            GPIO.output(buzzer_pin,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(buzzer_pin,GPIO.LOW)
      else:
            pass

def RFID_Card():
      lcd.text("scan a card",1)
      ID,msg = card.read()
      print(ID)
      if ID != 979717204583:
         lcd.text("wrong card",2)
         GPIO.output(relay_pin,GPIO.HIGH)
         GPIO.output(buzzer_pin,GPIO.HIGH)
         time.sleep(5)
         GPIO.output(buzzer_pin,GPIO.LOW)
         keypad()
      else:
           lcd.text("open",2)
           GPIO.output(relay_pin,GPIO.LOW) # door unlock #
           GPIO.output(buzzer_pin,GPIO.LOW)
           time.sleep(5)
           GPIO.output(relay_pin,GPIO.HIGH) # door gets lock after 5 seconds #
    
while True:
      RFID_Card()
      
