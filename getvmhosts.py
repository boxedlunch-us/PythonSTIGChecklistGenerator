from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import atexit
def GetVMHosts(content):
    host_view = content.viewManager.CreateContainerView(content.rootFolder,
                                                        [vim.HostSystem],
                                                        True)
    obj = [host for host in host_view.view]
    host_view.Destroy()
    return obj


# args = get_args()

def getvcenterconn():
    serviceInstance = SmartConnect(host='vcsa-01a.corp.local',
                                   user='administrator@vsphere.local',
                                   pwd='VMware1!',
                                   port=443)
    atexit.register(Disconnect, serviceInstance)
    content = serviceInstance.RetrieveContent()
    return content

def listvmhosts():
    serviceInstance = SmartConnect(host='vcsa-01a.corp.local',
                                   user='administrator@vsphere.local',
                                   pwd='VMware1!',
                                   port=443)
    atexit.register(Disconnect, serviceInstance)
    content = serviceInstance.RetrieveContent()

    hosts = GetVMHosts(content)

    return hosts

def getsinglehost(hostname):
    vmhosts = GetVMHosts(getvcenterconn())
    for v in vmhosts:
        if v.name == hostname:
            return v


def checks():
    hostList = listvmhosts()
    targetHosts = list()
    for h in hostList:
        targetHosts.append(v63173(h))

    return targetHosts


class complianceObj:
    def __init__(self, name, check, result):
        self.name = name
        self.check = check
        self.result = result

# def v63173(host):
#     for h in host.configManager.advancedOption.setting:
#         if h.key == 'DCUI.Access':
#             # print(h.key)
#             # print(h.value)
#             obj = complianceObj(host.name, h.key, h.value)
#             return obj

