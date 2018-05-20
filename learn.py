
import sys
import os
import time

from ir_devices import DeviceList
from ir_library import Librarian

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    library_dir = os.path.join(script_dir, 'ir_library')
    librarian = Librarian(library_dir)

    learn_time = 3
    remote = sys.argv[1]
    button = sys.argv[2]
    device_name = sys.argv[3] if len(sys.argv) > 3 else 'default'

    devices = DeviceList()
    device = devices.get(device_name)

    print("Entering learning mode for %s seconds..." % learn_time)
    device.enter_learning()
    time.sleep(learn_time)
    data = device.check_data()
    code = librarian.write(remote, button, data)

    print('')
    print(code)
    print('')

if __name__ == '__main__':
    main()
