import time
import os
import numpy as np
import pyautogui
import cv2


def OpenWeChat():

    os.startfile("C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe"
                 )  # 此处输入自己电脑上微信exe文件的绝对路径（！！！非快捷方式！！！）
    time.sleep(7)


# 自动点击匹配按钮
def imgAutoCick(tempFile, whatDo, debug=False):

    pyautogui.screenshot('big.png')
    gray = cv2.imread("big.png", 0)
    img_template = cv2.imread(tempFile, 0)
    w, h = img_template.shape[::-1]
    res = cv2.matchTemplate(gray, img_template, cv2.TM_SQDIFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    pyautogui.moveTo(top + h / 2, left + w / 2)

    whatDo(x)

    if debug:
        img = cv2.imread("big.png", 1)
        cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
        img = cv2.resize(img, (0, 0),
                         fx=0.5,
                         fy=0.5,
                         interpolation=cv2.INTER_NEAREST)
        cv2.imshow("processed", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    os.remove("big.png")


# 自动检测图片是否匹配
def imgAutoCheck(tempFile, debug=False):

    pyautogui.screenshot('check.png')
    gray = cv2.imread("check.png", 0)
    img_template = cv2.imread(tempFile, 0)
    w, h = img_template.shape[::-1]
    res = cv2.matchTemplate(gray, img_template, cv2.TM_SQDIFF)

    template_size = img_template.shape[:2]
    threshold = 0.99
    loc = np.where(res >= threshold)
    point = ()
    for pt in zip(*loc[::-1]):
        cv2.rectangle(gray, pt,
                      (pt[0] + template_size[1], pt[1] + +template_size[0]),
                      (7, 249, 151), 2)
        point = pt

    os.remove("check.png")

    if point == ():
        return 0


# 进入微信
def signIn():
    imgAutoCick("C:\\VSCODE\\vscode_cpp\\wifi-1\\joinbtn.png", pyautogui.click, False)
    time.sleep(5)
    #imgAutoCick("C:\\VSCODE\\vscode_cpp\\wifi-1\\small.png", pyautogui.click, False)
    time.sleep(1)