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
    iface = wifi.interfaces()[0]    #默认使用第一块网卡
    iface.scan()
    time.sleep(5)  # 应该是足够的，不需要全部搜索，经常用的wifi信号不会不好吧

    result = iface.scan_results()   # 未打开wifi会在这里出问题
    CommonlyUsedWifi = 0
    SchoolWifi = 0
    func = 0

    for i in range(len(result)):
        if result[i].ssid == "JYB-1031" or "huawei":
            CommonlyUsedWifi = 1
        elif result[i].ssid == "web.wlan.bjtu":
            SchoolWifi = 1

    if CommonlyUsedWifi == 1:
        print('常用网络')  
    elif CommonlyUsedWifi == 0 and SchoolWifi == 1:
        func = 1
        print('未连接到常用网络，连接校园网')
    
    if func == 1:
        # 开始连接校园网
    else:
        # 开始登录微信
