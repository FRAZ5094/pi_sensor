import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
# DHT_SENSOR=Adafruit_DHT.DHT11
DHT_PIN = 4


def get_DHT_temp_humid(max_attempts=30):
    attempt = 0
    temperature = None

    while attempt < max_attempts and temperature == None:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        attempt += 1


    if attempt == max_attempts:
        return {"temperature": "Sensor error", "humidity": "Sensor error"}
    else:
        humidity = float(humidity)
        temperature = float(temperature)
        return {"temperature": round(temperature, 2), "humidity": round(humidity, 2)}


if __name__ == "__main__":
    max_attempts = 20
    data = get_DHT_temp_humid(max_attempts=max_attempts)
    print(f"{data['temperature']},{data['humidity']}")
