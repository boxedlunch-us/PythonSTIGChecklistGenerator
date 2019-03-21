
class complianceObj:
    def __init__(self, name, check, result):
        self.name = name
        self.check = check
        self.result = result

def v63173(host):
    for h in host.configManager.advancedOption.setting:
        if h.key == 'DCUI.Access':
            # print(h.key)
            # print(h.value)
            obj = complianceObj(host.name, h.key, h.value)
            return obj
