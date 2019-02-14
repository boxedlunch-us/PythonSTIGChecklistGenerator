#!/usr/bin/env python


from __future__ import print_function
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import atexit
import sys
import argparse


# def get_args():
#     parser = argparse.ArgumentParser(
#         description='Arguments for talking to vCenter')
#
#     parser.add_argument('-s', '--host',
#                         required=True,
#                         action='store',
#                         help='vSpehre service to connect to')
#
#     parser.add_argument('-o', '--port',
#                         type=int,
#                         default=443,
#                         action='store',
#                         help='Port to connect on')
#
#     parser.add_argument('-u', '--user',
#                         required=True,
#                         action='store',
#                         help='User name to use')
#
#     parser.add_argument('-p', '--password',
#                         required=True,
#                         action='store',
#                         help='Password to use')
#
#     parser.add_argument('-v', '--vswitch',
#                         required=True,
#                         action='store',
#                         help='vSwitch to create')
#
#     args = parser.parse_args()
#     return args


def GetVMHosts(content):
    host_view = content.viewManager.CreateContainerView(content.rootFolder,
                                                        [vim.HostSystem],
                                                        True)
    obj = [host for host in host_view.view]
    host_view.Destroy()
    return obj


def getvmhost(content, hostname):
    host_view = content.viewManager.CreateContainerView(content.rootFolder,
                                                        [vim.HostSystem],
                                                        True)
    obj = [host.name for host in host_view.view if host.name == hostname]
    host_view.Destroy()
    return obj


def main():
    # args = get_args()
    serviceInstance = SmartConnect(host='vcsa-01a.corp.local',
                                   user='administrator@vsphere.local',
                                   pwd='VMware1!',
                                   port=443)
    atexit.register(Disconnect, serviceInstance)
    content = serviceInstance.RetrieveContent()

    hosts = GetVMHosts(content)



# Main section
if __name__ == "__main__":
    sys.exit(main())
