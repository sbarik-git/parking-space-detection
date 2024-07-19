import cv2
import pickle
import cvzone
import numpy as np

width,height = 115 , 50 #width and height of a single parking space

#Video feed
cap = cv2.VideoCapture('parkingmp4.mp4')
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

def checkParkingSpace(imgPro):
    spaceCounter = 0;
    for pos in posList:
        x,y = pos

        imgCrop = imgPro[y:y+height,x:x+width]
        #cv2.imshow(str(x*y),imgCrop)


        #counting the number of pixels in the rectangle (if more car is present)
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img,str(count),(x,y+height-2),scale=1 ,thickness=2,offset=0,colorT=(255,255,255),colorR=(0,0,255))

        if count<900:
            color = (0,255,0)
            thickness = 2
            spaceCounter += 1
        else:
            color = (0,0,255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height),color,thickness)

    cvzone.putTextRect(img, f'Available spots : {spaceCounter}/{len(posList)}', (50, 50), scale=2,thickness=1, offset = 2,
                       colorR=(0, 0, 0))


while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    sucess, img = cap.read()

    #converting image to grayscale
    imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur =cv2.GaussianBlur(imgGray,(3,3),1)#addign blur to the image

    #converting to binary image using adaptive thresholding
    imgThreshold =cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)

    #to remove noise using median blur
    imgMedian =cv2.medianBlur(imgThreshold,5)

    #using dilation to differentiate between empty space and a car making the boundaries more thicker
    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imgMedian,kernel,iterations=1)





    checkParkingSpace(imgDilate)

    cv2.imshow("Image",img)
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("imgThreshold", imgDilate)

    cv2.waitKey(15)
