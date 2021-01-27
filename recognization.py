import os
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_directory = os.path.join(BASE_DIR, "images")

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

recognizer = cv2.face.LBPHFaceRecognizer_create()
current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_directory):
    for file in files:
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            path = os.path.join(root, file)

            folderLabel = os.path.basename(os.path.dirname(path)).lower()
            print(folderLabel, path)

            if folderLabel in label_ids:
                pass
            else:
                label_ids[folderLabel] = current_id
                current_id += 1

            id_ = label_ids[folderLabel]
            print(label_ids)

            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image, "uint8")  # 8 bit integer
            # print(image_array)
            faces = faceCascade.detectMultiScale(image_array, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi = image_array[y:y + h, x:x + w]
                x_train.append(roi)
                y_labels.append(id_)

with open("labels.pickle", 'wb') as file:
    pickle.dump(label_ids, file)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")