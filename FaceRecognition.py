import sys
import time
import os
import numpy as np
from PIL import Image
import cv2
path = 'user_data'
name =''
if not os.path.exists("user_data"):
    os.mkdir('user_data')
def face_generator():
    global name
    cam = cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    dectector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_id=input("Enter id of user : ")
    name=input("Enter name : ")
    sample=int(input("Enter how many sample you wish to take  : "))
    for f in os.listdir(path): 
        os.remove(os.path.join(path, f))
    print("Taking sample image of user ...please look at Camera")
    time.sleep(2)
    count=0
    while True:
        ret,img=cam.read()
        converted_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=dectector.detectMultiScale(converted_image,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            count+=1
            cv2.imwrite("user_data/face."+str(face_id)+"."+str(count)+".jpg",converted_image[y:y+h,x:x+w])
            cv2.imshow("image",img)
        k=cv2.waitKey(1) & 0xff
        if k==27:
            break
        elif count>=sample:
            break
    print("Image Samples taken succefully !!!!.")
    cam.release()
    cv2.destroyAllWindows()
def traning_data():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    def images_and_labels(path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        face_samples = []
        ids = []
        for image_path in image_paths:
            gray_image = Image.open(image_path).convert('L')
            img_arr = np.array(gray_image, 'uint8')
            id = int(os.path.split(image_path)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_arr)
            for (x, y, w, h) in faces:
                face_samples.append(img_arr[y:y + h, x:x + w])
                ids.append(id)
        return face_samples, ids
    print("Training Data...please wait...!!!")
    faces, ids = images_and_labels(path)
    recognizer.train(faces, np.array(ids))
    recognizer.write('trained_data.yml')
    print("Data trained successfully!")
def detection():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trained_data.yml')  
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX  
    id = 5  
    names = ['',name]
    cam = cv2.VideoCapture(0)  
    cam.set(3, 640)
    cam.set(4, 480)
    minW = 0.1 * cam.get(3)
    maxW = 0.1 * cam.get(4)
    no = 0
    while True:
        if cam is None or not cam.isOpened():
            print('Warning: Unable to open video source: ')

        ret, img = cam.read()
        if ret == False:
            print("Unable to detect image")
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minW)),
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])
            if (accuracy < 100):
                id = names[id]
                accuracy = " {0}%".format(round(100 - accuracy))
                no += 1
            else:
                id = "unknown"
                accuracy = " {0}%".format(round(100 - accuracy))
                no += 1
            cv2.putText(img, "Press Esc to close this window", (5, 25), font, 1, (255, 0, 255), 2)
            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 0, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        cv2.imshow('camera', img)
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

def permisssion(val,task):
    if "Yes"==val or "yes" ==val:
         if task == 1:
             traning_data()
         elif task == 2:
             detection()
    else:
        print("ThankYou for using this application !! ")
        sys.exit()
print("\t\t\tWelcome to Face Authentication System ")
face_generator()
perm=input("Do you wish to train your image data for face authentication [Yes|No] : ")
permisssion(perm,1)
authenticate=input("Do your want test authentication system [Yes|No] : ")
permisssion(authenticate,2)
