#impoting necessary liberaries
import cv2
drive='N'
Timer=0
Status='ON'

#importing cascaing of face,eyes and smile
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#leye_cascade=cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
#reye_cascade=cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
#smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')


#building function for detecting face,eyes and smile.

#builiding for web cam
video_capture=cv2.VideoCapture(0)
    
flag=0
while True:
    _,frame=video_capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    
    if(drive=='N'):
     cv2.putText(frame, "Drive=N", (30,30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
     cv2.putText(frame, "Timer=5", (30,80),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
     cv2.putText(frame, "Status:ON", (30,120),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    if(drive=='F'):
        if(len(face)==1):
            cv2.putText(frame, "Drive=F", (30,30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, "Timer=5", (30,80),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, "Status:ON", (30,120),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            f=0
        if(len(face)==0):
            flag=flag+1
            
            if(flag<=50):
                if(flag%10==0):
                    f=f+1
                    print(str(f)+"no")
                cv2.putText(frame, "Drive=F", (30, 30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "Timer="+str(f), (30,80),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "Status:ON", (30,120),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            if(flag>50):
                f=int(flag%10)
                cv2.putText(frame, "Drive=F", (30, 30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "Timer=0", (30,80),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "Status:Stop", (30,120),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                f=0
        else:
            flag=0
    #for(x,y,w,h) in face:
     #   cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray=gray[y:y+h,x:x+w]
        #roi_color=frame[y:y+h,x:x+w]
        #leyes=leye_cascade.detectMultiScale(roi_gray,1.1,22)
        #reyes=reye_cascade.detectMultiScale(roi_gray,1.1,22)
        #smile=smile_cascade.detectMultiScale(roi_gray,1.7,22)
        #for(ex,ey,ew,eh) in leyes:
         #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        #for(ex,ey,ew,eh) in reyes:
         #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        #for(sx,sy,sw,sh) in smile:
         #   cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
       
    
    #canvas=detect(gray,frame)
    cv2.imshow('video',frame)
    
    if(cv2.waitKey(1)&0xff==ord('q')):
        break
video_capture.release()
cv2.destroyAllWindows()
    
