import smbus2
import bme280

def load_parameter(port, address):
    '''
    Load the calibration parameters from the BME280 sensor.
    @param port: The port number of the I2C bus.
    @param address: The address of the BME280 sensor.
    @return: The bus object.
    '''
    try:
        bus = smbus2.SMBus(port)
        bme280.load_calibration_params(bus, address)
        return bus
    except Exception as e:
        print(f"Error loading parameters: {e}")
        return None

def read_data(bus, address):
    try:
        sensor_data = bme280.sample(bus, address)
        humidity = sensor_data.humidity
        temperature = sensor_data.temperature
        return humidity, temperature
    except Exception as e:
        print(f"Error reading data: {e}")
        return None

