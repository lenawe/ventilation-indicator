import smbus2
import bme280

def load_parameter(port, address):
    try:
        bus = smbus2.SMBus(port)
        bme280.load_calibration_params(bus, address)
        return bus
    except Exception as e:
        print(f"Error loading parameters: {e}")
        return None

def read_data(bus, address):
    sensor_data = bme280.sample(bus, address)
    humidity = sensor_data.humidity
    temperature = sensor_data.temperature
    return humidity, temperature