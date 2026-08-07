import os
import cv2
from insightface.app import FaceAnalysis


class StudentRegistrar:

    def __init__(self):

        self.dataset_path = "dataset"

        self.detector = FaceAnalysis(name="buffalo_l")
        self.detector.prepare(ctx_id=0)

    def register(self, name):

        folder = os.path.join(self.dataset_path, name)
        os.makedirs(folder, exist_ok=True)

        cap = cv2.VideoCapture(0)

        count = 0

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            faces = self.detector.get(frame)

            for face in faces:

                x1, y1, x2, y2 = map(int, face.bbox)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

                cv2.putText(
                    frame,
                    f"Captured: {count}/20",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2
                )

            cv2.imshow("Register Student", frame)

            key = cv2.waitKey(1) & 0xFF

            print(key)

            if key == ord("S"):

                if len(faces) > 0:

                    face = faces[0]

                    x1, y1, x2, y2 = map(int, face.bbox)

                    face_crop = frame[y1:y2, x1:x2]

                    filename = os.path.join(folder, f"{count+1}.jpg")

                    cv2.imwrite(filename, face_crop)

                    print(f"Saved: {filename}")

                    count += 1

            elif key == ord("Q"):
                break

            if count >= 20:
                break

        cap.release()
        cv2.destroyAllWindows()