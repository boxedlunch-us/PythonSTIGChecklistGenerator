#!/usr/bin/env python


from __future__ import print_function
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import atexit
from getvmhosts import *
from stigchecks import *
import sys


# def v63173(host):
#     for h in host.configManager.advancedOption.setting:
#         if h.key == 'DCUI.Access':
#             # print(h.key)
#             # print(h.value)
#             obj = complianceObj(host.name, h.key, h.value)
#             return obj


def main():
    getsinglehost('esx-02a.corp.local')
    wang = v63173(getsinglehost('esx-02a.corp.local'))
    print(wang.check)


# Main section
if __name__ == "__main__":
    sys.exit(main())
