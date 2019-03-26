from getvmhosts import *


class complianceObj:
    def __init__(self, name, check, result):
        self.name = name
        self.check = check
        self.result = result


class AdvancedSetting:
    def __init__(self, key, value):
        self.key = key
        self.vlue = value

    def find(host, key):
        for h in host.configManager.advancedOption.setting:
            if h.key == key:
                obj = complianceObj(host.name, h.key, h.value)
                return obj


def v63173(host):
    hostess = getsinglehost('esx-02a.corp.local')
    dis = AdvancedSetting.find(hostess, 'DCUI.Access')
    return dis
