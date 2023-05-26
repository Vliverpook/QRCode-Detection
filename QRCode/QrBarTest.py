import cv2
import numpy as np
from pyzbar.pyzbar import decode
#pyzbar库用于处理二维码的编解码

# img=cv2.imread('1.png')
# code=decode(img)#对图片进行解码
# # print(code)
# #解码会返回由以下信息组成的队列（码所含有的信息、码的类型、矩形或多边形边界框的位置等）
# #[Decoded(data=b'111111', type='QRCODE', rect=Rect(left=207, top=434, width=182, height=184), polygon=[Point(x=207, y=434), Point(x=207, y=618), Point(x=389, y=618), Point(x=389, y=434)], quality=1, orientation='UP')]
# for barcode in code:
#     print(barcode.data)#返回所有码所含有的信息，b'111111'其中b表示以字节为单位，可以再通过decode('utf-8')进行解码

cap=cv2.VideoCapture(0)#调用电脑摄像头
cap.set(3,640)
cap.set(4,480)
#设置宽高
while True:
    success, img=cap.read()#获取每帧的图像
    for barcode in decode(img):
        myData=barcode.data.decode('utf-8')
        print(myData)
        #下面绘制多边形框并添加信息，多边形比矩形边框能更好的适合变化场景的锚定
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2=barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)#暂停1毫秒