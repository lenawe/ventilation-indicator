import smbus2
import bme280

def load_parameter(port, address):
    bus = smbus2.SMBus(port)
    bme280.load_calibration_params(bus, address)
    return bus
