from rp_local.sensor.read import load_parameter, read_data
from rp_local.sensor.process import get_payload_json

if __name__ == '__main__':
    port = 1
    address = 0x76

    bus = load_parameter(port, address)
    humidity, temperature = read_data(bus, address)

    json_payload = get_payload_json(humidity, temperature)
    
    print(json_payload)