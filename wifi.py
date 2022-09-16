def isConnected():
    import requests
    try:
        html = requests.get("http://www.baidu.com", timeout=2)
    except:
        return False
    return True


def WifiName():
    # 导入模块
    import pywifi
    import time

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(2)

    result = iface.scan_results()

    for i in range(len(result)):
        print(result[i].ssid)
        if result[i].ssid == "JYB-1031" or "huawei":
            break
    return True
    #ssid 是名称 ，signal 是信号强度
