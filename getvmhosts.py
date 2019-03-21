from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
from stigchecks import v63173
import atexit
def GetVMHosts(content):
    host_view = content.viewManager.CreateContainerView(content.rootFolder,
                                                        [vim.HostSystem],
                                                        True)
    obj = [host for host in host_view.view]
    host_view.Destroy()
    return obj


# args = get_args()


def listvmhosts():
    serviceInstance = SmartConnect(host='vcsa-01a.corp.local',
                                   user='administrator@vsphere.local',
                                   pwd='VMware1!',
                                   port=443)
    atexit.register(Disconnect, serviceInstance)
    content = serviceInstance.RetrieveContent()

    hosts = GetVMHosts(content)

    return hosts

def checks():
    hostList = listvmhosts()
    targetHosts = list()
    for h in hostList:
        targetHosts.append(v63173(h))

    return targetHosts
