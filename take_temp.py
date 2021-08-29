import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read(Adafruit_DHT.DHT11, 4)
print("humid", humidity, "temp", temperature)
