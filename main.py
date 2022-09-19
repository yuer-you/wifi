from wifi import WifiSchool, WifiSearch, isConnected
from wechat import OpenWeChat, signIn

WS = WifiSearch()

if WS == 0:
    if isConnected():
        OpenWeChat()
        signIn()
elif WS == 1:
    if WifiSchool():
        if isConnected():
            OpenWeChat()
            signIn()
elif WS == -1:
    print('未搜索到常用网络及校园网，请手动连接')
