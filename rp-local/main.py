import bme280.read as b_read
import bme280.process as b_process

if __name__ == '__main__':
    port = 1
    address = 0x76

    bus = b_read.load_parameter(port, address)
    humidity, temperature = b_read.read_data(bus, address)

    json_payload = b_process.get_payload_json(humidity, temperature)
    
    print(json_payload)