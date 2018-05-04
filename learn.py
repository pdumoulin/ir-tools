
import sys
import time

from devices import DeviceList

def main():
    learn_time = 10
    remote = sys.argv[1]
    button = sys.argv[2]
    device_name = sys.argv[3] if len(sys.argv) > 3 else 'default'

    devices = DeviceList()
    device = devices.get(device_name)
    device.auth()

    print("Entering learning mode for %s seconds..." % learn_time)
    device.enter_learning()
    time.sleep(learn_time)
    data = device.check_data()
    hex_data = data.encode('hex')
    print(hex_data)
    
    # TODO - save data in library

if __name__ == '__main__':
    main()
