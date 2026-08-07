import os
import cv2
import time
from datetime import datetime


class UnknownLogger:

    def __init__(self):

        self.folder = "unknown_faces"
        os.makedirs(self.folder, exist_ok=True)

        self.last_saved = 0

    def save(self, frame, bbox):

        if time.time() - self.last_saved < 5:
            return

        self.last_saved = time.time()

        x1, y1, x2, y2 = map(int, bbox)

        face = frame[y1:y2, x1:x2]

        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"

        path = os.path.join(self.folder, filename)

        cv2.imwrite(path, face)

        print("Unknown face saved:", filename)