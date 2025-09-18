import os
from ultralytics import YOLO
import cv2
import cvzone
import math
import numpy as np
from sort import *

# Création du dossier de sortie s'il n'existe pas
output_folder = "car_count_result"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialisation de l'écriture vidéo
cap = cv2.VideoCapture("Videos\cars.mp4") #for video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter(os.path.join(output_folder, 'output.avi'), cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

model = YOLO('Yolo Weights\yolov8l.pt')

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

mask = cv2.imread("3 Car Counter Project\mask.png")

# Tracking
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

limits = [400, 297, 673, 297]
totalCount = []

# Inference on video
while True:
    success, img = cap.read()
    if not success:
        break

    # Ensure mask dimensions match image dimensions
    mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

    imgRegion = cv2.bitwise_and(img, mask)
    imgGraphics = cv2.imread("3 Car Counter Project\graphics.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (0, 0))
    results = model(imgRegion, stream=True)
    detections = np.empty((0, 5))

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding boxes
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100

            # Class name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if (currentClass == 'car' or currentClass == 'bus' or currentClass == 'motorbike'
                    or currentClass == 'truck') and conf > 0.3:
                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))

    resultTracker = tracker.update(detections)
    # Counting line
    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 5)

    for result in resultTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 255))
        cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), max(35, y1)),
                           scale=2.0, thickness=3, offset=10)

        cx, cy = x1 + w // 2, y1 + h // 2
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        # Vehicle counting logic
        if limits[0] < cx < limits[2] and limits[1] - 15 < cy < limits[3] + 15:
            if totalCount.count(id) == 0:
                totalCount.append(id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)

    cv2.putText(img, str(len(totalCount)), (255, 100), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 255), 8)

    # Écrire le frame traité dans le fichier vidéo
    out.write(img)

    cv2.imshow("Image", img)
    # cv2.imshow("ImageRegion", imgRegion)
    cv2.waitKey(1)

# Libérer les ressources
cap.release()
out.release()
cv2.destroyAllWindows()
