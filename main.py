from wifi import WifiSchool, WifiSearch, isConnected
from wechat import ConnectWeChat

if WifiSearch() == 0:
    if isConnected():
        ConnectWeChat()
elif WifiSearch() == 1:
    if WifiSchool():
        if isConnected():
            
elif WifiSearch == 