import cv2
import winsound

webcam=cv2.VideoCapture(0)

while True:
    _,img1=webcam.read()
    _,img2=webcam.read()
    cv2.imshow("Security Camera",img1)
    if cv2.waitKey(10)==27:
        break
webcam.release()
cv2.destroyAllWindows()