import libvirt
import sys
conn=libvirt.open("qemu:///system")
argvs = sys.argv

def check_instance_status(instance_name):
    for dom in conn.listAllDomains() :
        status=dom.info()

        if (instance_name == dom.name()) and (status[0] == 5):
            return True
    return False

def vm_convert(instance_name):
    return True

if __name__ == '__main__':

    instance_name = sys.argv[1]
    ret = check_instance_status(instance_name)
    if ret is True:
        print("convert available")
    else:
        print("Please input available vm or no vm in here")
