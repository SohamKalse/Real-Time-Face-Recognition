import cv2
from tkinter import *
import pickle
import tkinter.messagebox
import tkinter as tk

##################################################################################################

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
labels = {"person_name": 1}
with open("labels.pickle", 'rb') as file:  # read binary mode
    orignal_labels = pickle.load(file)
    labels = {value: key for key, value in orignal_labels.items()}  # to inverse the format of ori_Labels dict


def image():
    img = cv2.imread("w.jpg", 1)
    # print(img)

    imagePath = "w.jpg"
    cascPath = "haarcascade_frontalface_default.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    print("Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    tk.messagebox.showinfo('title', "Found {0} faces !!".format(len(faces)))

    cv2.waitKey(0)


##################################################################################

def web_cam_face_detect():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        print("Found {0} faces!".format(len(faces)))

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_color = img[y:y + h, x:x + w]
            roi_gray = gray[y:y + h, x:x + w]

            id_, confidence = recognizer.predict(roi_gray)
            if confidence >= 35 and confidence <= 85:
                # print(id_)
                # print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 1
                cv2.putText(img, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            imgitem = "myimage.png"
            cv2.imwrite(imgitem, roi_color)

        cv2.imshow('img', img)

        if cv2.waitKey(1) == ord('x'):
            break

    cap.release()
    cv2.destroyAllWindows()


#######################################################################################################

def faceDetectWithMobileCam():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture('http://192.168.43.150:4747/video')

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        print("Found {0} faces!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            imgitem = "myimage.png"
            roi_color = img[y:y + h, x:x + w]
            roi_gray = gray[y:y + h, x:x + w]

            id_, confidence = recognizer.predict(roi_gray)
            if confidence >= 35 and confidence <= 85:
                # print(id_)
                # print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 1
                cv2.putText(img, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            cv2.imwrite(imgitem, roi_color)

        cv2.imshow('img', img)

        if cv2.waitKey(1) == ord('x'):
            break

    cap.release()
    cv2.destroyAllWindows()


########################################################################################################
def eye_detection():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        print("Found {0} faces!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            print("Found {0} eyes!".format(len(eyes)))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow('img', img)

        if cv2.waitKey(1) == ord('x'):
            break

    cap.release()
    cv2.destroyAllWindows()


#########################################################################################3
root = Tk()
root.title("Face")
root.geometry("1300x500")

def gui2():
    background_image = tk.PhotoImage(file='icons\\fg2.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, height=700)

    photo = PhotoImage(file="icons\\ip2.png")
    photo2 = PhotoImage(file="icons\\fr2.png")
    photo3 = PhotoImage(file="icons\\fe2.png")
    photo4 = PhotoImage(file="icons\\frm2.png")
    photo5 = PhotoImage(file="icons\\exi.png")
    btn = Button(
        root,
        image=photo,
        border=0,
        command=image
    )

    btn.pack(pady=0)

    btn2 = Button(
        root,
        image=photo2,
        border=0,
        command=web_cam_face_detect
    )
    btn2.pack(pady=4)

    btn3 = Button(
        root,
        border=0,
        image=photo3,
        command=eye_detection
    )
    btn3.pack(pady=0)

    btn4 = Button(
        root,
        image=photo4,
        border=0, command=faceDetectWithMobileCam

    )
    btn4.pack(pady=4)

    btn5 = Button(
        root,
        image=photo5,
        border=0,

        command=exit
    )
    btn5.pack(pady=0)

    root.mainloop()


gui2()


def printInstruction():
    print("1. total number of students present")
    print("2. Face recognition ")
    print("3. Face and Eye detection")
    print("4. face recognition using mobile camera")
    print("5. exit")


while (True):

    printInstruction()
    choice = int(input("Enter your choice : "))
    if (choice == 1):
        image()

    elif (choice == 2):
        web_cam_face_detect()

    elif choice == 3:
        eye_detection()

    elif (choice == 4):
        faceDetectWithMobileCam()

    elif (choice == 5):
        exit()

############################################################################################
