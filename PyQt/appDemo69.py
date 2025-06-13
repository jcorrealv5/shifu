import cv2

video = cv2.VideoCapture(0)
if(video.isOpened()):
    while True:
        rpta, imagen = video.read()
        if(rpta):
           cv2.imshow("Video", imagen) 
           key = cv2.waitKey(1)
           if(key == ord("s")):
               break
    video.release()
    cv2.destroyAllWindows()
else:
    print("No esta activa la Camara Web")