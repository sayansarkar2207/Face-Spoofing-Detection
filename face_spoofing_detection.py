import cv2,imutils
cam=cv2.VideoCapture(0)
while True:
    img=cam.read()[1]
    (color,text) =((0,0,255),"Spoofing Detected") if (max([cv2.contourArea(c) for c in imutils.grab_contours(cv2.findContours(cv2.GaussianBlur(cv2.dilate(cv2.erode(cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),160,255,cv2.THRESH_BINARY)[1],None,iterations=5),None,iterations=5),(21,21),0).copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE))]or[0])>7000) else ((0,255,0),"No Spoofing Detected")
    if text=="No Spoofing Detected":[cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) for (x,y,w,h) in cv2.CascadeClassifier("haarcascade_frontalface_default.xml").detectMultiScale(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),1.3,5)]
    cv2.putText(img,text, (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 1,color, 2)
    cv2.imshow("FaceDetection",img)
    if cv2.waitKey(10)==27:break
cam.release()
cv2.destroyAllWindows()
