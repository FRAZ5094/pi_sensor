import Adafruit_DHT
import time

DHT_SENSOR=Adafruit_DHT.DHT11
DHT_PIN=4

max_attempts=30
attempt=0

temperature=None

while attempt<max_attempts and temperature==None:
    humidity,temperature= Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
    attempt+=1

if attempt==max_attempts:
    print("Sensor error")
else:
    print(f"{int(time.time())},{int(temperature)},{int(humidity)}")
