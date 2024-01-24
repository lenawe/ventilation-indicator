import bme280.read as b_read
if __name__ == '__main__':
    port = 1
    address = 0x76

    bus = b_read.load_parameter(port, address)
    humidity, temperature = b_read.read_data(bus, address)
