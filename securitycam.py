import cv2
import winsound

webcam=cv2.VideoCapture(0)

while True:
    _,img1=webcam.read()
    _,img2=webcam.read()
    diff=cv2.absdiff(img1,img2)
    cv2.imshow("Security Camera",diff)
    if cv2.waitKey(10)==27:
        break
webcam.release()
cv2.destroyAllWindows()