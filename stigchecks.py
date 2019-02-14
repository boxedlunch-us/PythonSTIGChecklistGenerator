def v63173(host):
    for h in host.configManager.advancedOption.setting:
        if h.key == 'DCUI.Access':
            print(h.key)
            print(h.value)
