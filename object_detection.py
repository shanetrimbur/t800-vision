import tensorflow as tf
import numpy as np
import cv2

# Load the saved model
model_dir = '/home/one/Downloads/ssd_mobilenet_v2_320x320_coco17_tpu-8/saved_model/'
detect_fn = tf.saved_model.load(model_dir)

# Load labels (example)
category_index = {
    1: {'id': 1, 'name': 'person'},
    2: {'id': 2, 'name': 'bicycle'},
    3: {'id': 3, 'name': 'car'},
    # Add more classes as per the model's training set
}

# Initialize video capture with the correct index
cap = cv2.VideoCapture(1)  # Now using camera index 1

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert frame to tensor
    input_tensor = tf.convert_to_tensor(frame)
    input_tensor = input_tensor[tf.newaxis, ...]

    # Run inference
    detections = detect_fn(input_tensor)

    # Extract detection results
    boxes = detections['detection_boxes'][0].numpy()
    classes = detections['detection_classes'][0].numpy().astype(int)
    scores = detections['detection_scores'][0].numpy()

    # Visualize detection results
    for i in range(len(scores)):
        if scores[i] > 0.5:  # Confidence threshold
            ymin, xmin, ymax, xmax = boxes[i]
            startX, startY = int(xmin * frame.shape[1]), int(ymin * frame.shape[0])
            endX, endY = int(xmax * frame.shape[1]), int(ymax * frame.shape[0])

            # Print the detected class ID
            class_id = classes[i]
            print(f"Detected class ID: {class_id}")

            # Use a fallback if class ID is not in category_index
            label = category_index.get(class_id, {'name': 'Unknown'})['name']
            
            cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
            cv2.putText(frame, f'{label}: {scores[i]:.2f}', (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow('Object Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
