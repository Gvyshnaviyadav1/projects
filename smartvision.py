import cv2
import numpy as np
from win10toast import ToastNotifier

notifier = ToastNotifier()

# Load YOLOv4 model
weights_path = "yolov4.weights"
config_path = "yolo4.cfg"
coco_names = "coco.names"

# Load class names
with open(coco_names, "r") as f:
    classes = f.read().strip().split("\n")

# Load the YOLO model using OpenCV
net = cv2.dnn.readNet(weights_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)  

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    # Prepare image for YOLO
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Run forward pass to get detections
    outputs = net.forward(net.getUnconnectedOutLayersNames())

    boxes, confidences, class_ids = [], [], []

    # Process YOLO output
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and class_id == 0:  # Detect only persons (class_id = 0,humans only )
                center_x, center_y, w, h = (detection[:4] * np.array([width, height, width, height])).astype("int")
                x, y = int(center_x - w / 2), int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Maximum Suppression  to remove overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = f"Person: {confidences[i]:.2f}"
            color = (0, 255, 0)  # Green bounding box

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    if len(indices)>1: #if more than one human detected send warning s
        notifier.show_toast("WARNING more than one person in frame")

    # Show the frame
    cv2.imshow("Human Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
