import cv2
import numpy as np

i = 0;
# kırmızı renk algılanan objenin etrafına dörtgen çizip yazı yazıyor.
def rectangle_red(res):

    lr = cv2.pyrDown(res)
    lr2 = cv2.pyrDown(lr)


    kernel_ero = np.ones((3, 3), np.uint8)
    kernel_dil = np.ones((7, 7), np.uint8)

    blur = cv2.medianBlur(lr2, 5)
    erosion = cv2.erode(blur, kernel_ero, iterations=1)
    dilation = cv2.dilate(erosion, kernel_dil, iterations=1)

    gray = cv2.cvtColor(dilation, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("asd",gray)

    # Buradan oncesi goruntuyu duzeltme islemiydi. Buradan sonrası görüntüyü kesme islemi.
    h = gray.shape[0]
    w = gray.shape[1]
    color = []
    for y in range(0, h):
        for x in range(0, w):
            if gray[y, x] > 10:
                color.append((y, x))
    y_buyuk = 0
    y_kucuk = 9999
    x_buyuk = 0
    x_kucuk = 9999

    for x1 in color:
        if x1[0] > y_buyuk:
            y_buyuk = x1[0]
        if x1[1] > x_buyuk:
            x_buyuk = x1[1]
        if x1[0] < y_kucuk:
            y_kucuk = x1[0]
        if x1[1] < x_kucuk:
            x_kucuk = x1[1]
    lr2 = cv2.rectangle(lr2, (x_kucuk, y_kucuk), (x_buyuk, y_buyuk), (0, 0, 255), 1)
    cv2.putText(lr2, 'Red Object', (x_kucuk, y_kucuk - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)

    pr = cv2.pyrUp(lr2)
    pr2 = cv2.pyrUp(pr)
    return pr2

# mavi renk algılanan objenin etrafına dörtgen çizip yazı yazıyor.
def rectangle_blue(res):

    lr = cv2.pyrDown(res)
    lr2 = cv2.pyrDown(lr)


    kernel_ero = np.ones((3, 3), np.uint8)
    kernel_dil = np.ones((7, 7), np.uint8)

    blur = cv2.medianBlur(lr2, 5)
    erosion = cv2.erode(blur, kernel_ero, iterations=1)
    dilation = cv2.dilate(erosion, kernel_dil, iterations=1)

    gray = cv2.cvtColor(dilation, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("asd",gray)

    # Buradan oncesi goruntuyu duzeltme islemiydi. Buradan sonrası görüntüyü kesme islemi.
    h = gray.shape[0]
    w = gray.shape[1]
    color = []
    for y in range(0, h):
        for x in range(0, w):
            if gray[y, x] > 10:
                color.append((y, x))
    y_buyuk = 0
    y_kucuk = 9999
    x_buyuk = 0
    x_kucuk = 9999

    for x1 in color:
        if x1[0] > y_buyuk:
            y_buyuk = x1[0]
        if x1[1] > x_buyuk:
            x_buyuk = x1[1]
        if x1[0] < y_kucuk:
            y_kucuk = x1[0]
        if x1[1] < x_kucuk:
            x_kucuk = x1[1]
    lr2 = cv2.rectangle(lr2, (x_kucuk, y_kucuk), (x_buyuk, y_buyuk), (255, 0, 0), 1)
    cv2.putText(lr2, 'Blue Object', (x_kucuk, y_kucuk - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1, cv2.LINE_AA)

    pr = cv2.pyrUp(lr2)
    pr2 = cv2.pyrUp(pr)
    return pr2


# video ve renk algılama kısmı

cap = cv2.VideoCapture(0)

while(1):

    #Her kareyi al
    _,frame = cap.read()

    # blur = cv2.medianBlur(frame, 9)

    i = i + 1
    #BGR'den HSV'ye dönüştür
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    lower_blue = np.array([90,100,100])
    upper_blue = np.array([130,255,255])

    lower_red = np.array([150,80,80])
    upper_red = np.array([179,255,255])

    lower_green = np.array([55,80,80])
    upper_green = np.array([90,255,255])

    lower_yellow = np.array([0,100,100])
    upper_yellow = np.array([30,255,255])



    #HSV'de ilk değişken için: 0-50 arası sarı, 50-100 arası yeşil, 100-140 arası mavi, 140-179 arası kırmızı

    mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)
    mask_red = cv2.inRange(hsv,lower_red,upper_red)
    mask_green = cv2.inRange(hsv,lower_green,upper_green)
    mask_yellow = cv2.inRange(hsv,lower_yellow,upper_yellow)


    res_blue = cv2.bitwise_and(frame,frame,mask=mask_blue)
    res_red = cv2.bitwise_and(frame,frame,mask=mask_red)
    res_green = cv2.bitwise_and(frame,frame,mask=mask_green)
    res_yellow = cv2.bitwise_and(frame,frame,mask=mask_yellow)

    res_red = rectangle_red(res_red)
    res_blue = rectangle_blue(res_blue)


    cv2.imshow('frame',frame)
    cv2.imshow('blue',res_blue)
    cv2.imshow('red',res_red)
    cv2.imshow('green',res_green)
    cv2.imshow('yellow',res_yellow)




    k = cv2.waitKey(5) & 0xFF
    if k == 27:  # wait for ESC key to exit
        break
    elif k == ord('b'):  # wait for 's' key to save and exit
        cv2.imwrite('blue.png', res_blue)
    elif k == ord('r'):  # wait for 's' key to save and exit
        cv2.imwrite('red.png', res_red)
    elif k == ord('g'):  # wait for 's' key to save and exit
        cv2.imwrite('green.png', res_green)
    elif k == ord('y'):  # wait for 's' key to save and exit
        cv2.imwrite('yellow.png', res_yellow)


cv2.destroyAllWindows()


# Bir rengin HSV kodunu bulmak için aşağıdaki kodları kullanmanız yeterli olacaktır.
#       >>> green = np.uint8([[[0,255,0]]])
#       >>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
#       >>> print(hsv_green)
# ÇIKTI: [[[ 60 255 255 ]]]
#   Alt ve Üst sınırları belirlemek için [H-10,100,100] ve [H+10,255,255] kullanabilirsiniz.




