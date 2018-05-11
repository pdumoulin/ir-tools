
import sys
import os

from devices import DeviceList
from library import Librarian

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    library_dir = os.path.join(script_dir, 'library')
    librarian = Librarian(library_dir)

    remote = sys.argv[1]
    button = sys.argv[2]
    device_name = sys.argv[3] if len(sys.argv) > 3 else 'default'

    devices = DeviceList()
    device = devices.get(device_name)

    code = librarian.read(remote, button)
    device.send_data(code)
    print('sent!')

if __name__ == '__main__':
    main()
