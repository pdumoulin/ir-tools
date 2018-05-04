
import broadlink

CONFIG = [
    {
        'ip'      : '192.168.1.88',
        'port'    : '80',
        'mac_hex' : 'bfe18e34ea34',
        'devtype' : '10039',
        'class'   : 'rm',
        'name'    : 'default'
    }
]

class DeviceList(object):

    devices = {}

    def __init__(self):
        for device_config in CONFIG:
            device_name = device_config['name']
            device = self.create_device(device_config)
            if device_name in self.devices:
                raise Exception("Device name %s is not unique!" % device_name)
            self.devices[device_name] = device

    def get(self, name):
        return self.devices[name] if name in self.devices else None

    def create_device(self, device_config):
        host = (device_config['ip'], int(device_config['port']))
        mac = device_config['mac_hex'].decode('hex')
        devtype = int(device_config['devtype'])
        return broadlink.rm(host, mac, devtype)
