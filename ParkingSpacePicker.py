import cv2
import pickle #to save all the parking spaces and bring it in the main code

width,height = 115 , 50 #width and height of a single parking space
try :
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseCLick(events,x,y,flags,param):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1 < x < x1+width and y1 < y < y1+height:
                posList.pop(i)

    with open('CarParkPos','wb') as f:
        pickle.dump(posList,f)

while True:
    img = cv2.imread('parkingimg.png')
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,0),2)

    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image", mouseCLick)
    cv2.waitKey(1)
