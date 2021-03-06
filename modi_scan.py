import subprocess
from time import sleep


def num_modi_in_usb():

    proc = subprocess.Popen("lsusb | grep 2fde:0002", 
                             shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    output = stdout.decode()

    # if error
    if stderr != b'':
        return stderr.decode()

    if len(output) == 0:
        return 0

    _list = output.rstrip('\n').split('\n')
    return len(_list)


def print_modi_list():

    num = num_modi_in_usb()

    if num <= 0: return
    
    import modi

    bundle_list = list()
    for i in range(num):
        print(i)
        bundle = modi.MODI()
        bundles = bundle.modules
        for m in bundles:
            if m.is_connected:
                bundle_list.append((m.module_type, m.uuid, m.id, m.is_up_to_date))
    print (bundle_list)

    bundle.close()

    for m in bundle_list:
        if not m[3]:
            if m[0] == 'network':
                modi.update_network_firmware()
            else:
                modi.update_module_firmware(target_ids=(m[2], ))

    return bundle_list

    
#     # thread creation

#     # run modi inside the thread

#     # def thread_func(network_uuid):
#     #     import modi
#     #     b = modi.MODI(ble, network_uuid)
#     # threading.Thread.run(target_func=thread_func, args=(network_uuid,),)

#     # if error
#     if stderr != b'':
#         return stderr.decode()

#     if len(output) == 0:
#         return 0

#     _list = output.rstrip('\n').split('\n')
#     return len(_list)




