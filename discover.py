
import sys
import broadlink
import binascii

def main():
    default_timeout = 10
    timeout = int(sys.argv[1]) if len(sys.argv) > 1 else default_timeout
    devices = broadlink.discover(timeout=timeout)
    print("Found %s devices!" % len(devices))
    print("")
    for device in devices:
        print("device.host      => %s (%s)" % (device.host, type(device.host)))
        print("device.host.ip   => %s (%s)" % (device.host[0], type(device.host[0])))
        print("device.host.port => %s (%s)" % (device.host[1], type(device.host[1])))
        print("device.devtype   => %s (%s)" % (device.devtype, type(device.devtype)))
        print("device.mac       => %s (%s)" % (device.mac, type(device.mac)))
        print("device.mac       => %s (%s)" % (binascii.hexlify(device.mac), 'hex'))
        print("device class     => %s " % device)
        print("")

if __name__ == '__main__':
    main()
