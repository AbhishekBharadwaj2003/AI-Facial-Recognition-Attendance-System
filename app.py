import cv2

from utils.camera import Camera
from utils.detector import FaceDetector
from utils.recognizer import FaceRecognizer
from utils.database import AttendanceDatabase
from utils.unknown_logger import UnknownLogger

camera = Camera()
detector = FaceDetector()
recognizer = FaceRecognizer()
database = AttendanceDatabase()
unknown_logger = UnknownLogger()

recognizer.load_database()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    faces = detector.detect(frame)

    for face in faces:

        x1, y1, x2, y2 = map(int, face.bbox)

        embedding = face.embedding

        # IMPORTANT
        name, score = recognizer.recognize(embedding)

        if name == "Unknown":
            unknown_logger.save(frame, face.bbox)
        else:
            database.mark_attendance(name)

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"{name} ({score:.2f})",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Recognition Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
database.close()