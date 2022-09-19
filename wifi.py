# 判断是否联网，bool值
import time
import requests

def isConnected():
    time.sleep(5)
    try:
        html = requests.get("http://www.baidu.com", timeout=2)
    except:
        return False
    return True


# 搜索附近网络，0直接登录微信，1连接校园网后登录微信，-1未搜索到无线网络
def WifiSearch():
    import pywifi
    import sys

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # 默认使用第一块网卡
    iface.scan()
    time.sleep(3)  # 应该是足够的，不需要全部搜索，经常用的wifi信号不会不好吧

    try:
        result = iface.scan_results()
    except:
        print('未打开本机wifi')
        sys.exit(1)

    CommonlyUsedWifi = 0
    SchoolWifi = 0

    for i in range(len(result)):
        if result[i].ssid == ('JYB-1031' or 'huawei'):
            CommonlyUsedWifi = 1
        elif result[i].ssid == "web.wlan.bjtu":
            SchoolWifi = 1

    if CommonlyUsedWifi == 1:
        print('常用网络')
        return 0  # 登陆微信

    elif CommonlyUsedWifi == 0 and SchoolWifi == 1:
        print('未搜索到常用网络，连接校园网')
        profile = pywifi.Profile()  # 配置文件
        profile.ssid = "web.wlan.bjtu"  # wifi名称
        # iface.remove_all_network_profiles()  # 删除其它配置文件
        tmp_profile = iface.add_network_profile(profile)  # 加载配置文件
        iface.connect(tmp_profile)
        return 1  # 连接校园网

    elif CommonlyUsedWifi == 0 and SchoolWifi == 0:
        print('附近没有可用无线网络')
        return -1  # 附近无可用无线网


# 连接校园网，bool值
def WifiSchool():
    url = 'http://10.10.42.3/drcom/login?callback=dr1663404133887&DDDDD=20281173&upass=85791738&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=1663404122001'
    try:
        response = requests.get(url).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
        time.sleep(8)
    except:
        if isConnected():
            return True
        else:
            return False
    print("状态码{}".format(response))  # 打印状态码
    if response == 200:
        return True
    else:
        return False
