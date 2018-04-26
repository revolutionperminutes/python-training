import sys
import libvirt
from nova import utils

conn = libvirt.open("qemu:///system")

def check_instance_status(instance_name):
    dom = conn.lookupByName(instance_name)
    state, reason = dom.state()

    if state == libvirt.VIR_DOMAIN_SHUTOFF:
        return True
    else:
        print('The state is not SHUTOFF.')
    return False

def vm_convert(instance_name):
    from_path = "/var/lib/nova/instances/" + instance_name + "/disk"
    tmp_path = "/var/lib/nova/tmp/" + instance_name + "_disk"
    print(from_path)
    print(tmp_path)
    utils.execute('qemu-img', 'convert', '-f', 'qcow2','-O', 'raw', from_path, tmp_path)

if __name__ == '__main__':

    instance_name = sys.argv[1]
    ret = check_instance_status(instance_name)
    if ret is True:
        vm_convert(instance_name)
