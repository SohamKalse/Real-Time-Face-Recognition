from tkinter import *
import tkinter as tk
# from face import image,web_cam_face_detect,faceDetectWithMobilecam,eye_detection
# import face
# import recognization
# from PIL import Image
# import os
# from PIL import Image
# import numpy as np
# import cv2
# import pickle

root = Tk()
root.geometry("1200x500")

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
    # command=image
)

btn.pack(pady=0)

btn2 = Button(
    root,
    image=photo2,
    border=0,
    # command=web_cam_face_detect
)
btn2.pack(pady=0)

btn3 = Button(
    root,
    border=0,
    image=photo3,
    # command=eye_detection
)
btn3.pack(pady=0)

btn4 = Button(
    root,
    image=photo4,
    border=0,
    # command=faceDetectWithMobilecam

)
btn4.pack(pady=0)

btn5 = Button(
    root,
    image=photo5,
    border=0,
    # command=exit
)
btn5.pack(pady=0)

root.mainloop()

