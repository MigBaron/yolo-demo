from ultralytics import YOLO
import cv2

# Chargement global
model = YOLO("./weights/yolov8n.pt")


def generate_frames():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        raise ValueError("No frame detected")
        return
    while True:
        success, frame = camera.read()
        if not success:
            break

        results = model(frame, stream=True)

        for result in results:
            annotated_frame = result.plot()

            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    camera.release()