import datetime, time
import cv2
import os

def capture_webcam_images():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        return

    interval_seconds = 60
    total_photos = 100
    folder_name = datetime.datetime.now().strftime("%Y-%m-%d_webcam")
    
    for _ in range(5):
        camera.read()
        time.sleep(0.1)

    for _ in range(total_photos):
        success, frame = camera.read()
        if not success:
            continue
        timestamp = datetime.datetime.now().strftime("%H%M%S")
        filename = f"webcam_{timestamp}.jpg"
        save_image(folder_name, filename, frame)
        time.sleep(interval_seconds)

    camera.release()

def save_image(folder, filename, image_data):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    cv2.imwrite(path, image_data)