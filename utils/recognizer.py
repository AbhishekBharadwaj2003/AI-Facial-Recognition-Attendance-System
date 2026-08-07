import os
import cv2
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from insightface.app import FaceAnalysis


class FaceRecognizer:

    def __init__(self):

        self.database = {}

        self.app = FaceAnalysis(name="buffalo_l")
        self.app.prepare(ctx_id=0)

    def generate_embeddings(self, dataset_path="dataset"):

        self.database = {}

        for person in os.listdir(dataset_path):

            person_path = os.path.join(dataset_path, person)

            if not os.path.isdir(person_path):
                continue

            embeddings = []

            print(f"\nProcessing {person}")

            for image_name in os.listdir(person_path):

                image_path = os.path.join(person_path, image_name)

                print(f"Reading: {image_path}")

                image = cv2.imread(image_path)

                if image is None:
                    print(f"❌ Cannot read image: {image_path}")
                    continue

                faces = self.app.get(image)

                if len(faces) == 0:
                    continue

                embeddings.append(faces[0].embedding)

            self.database[person] = embeddings

    def save_database(self):

        os.makedirs("embeddings", exist_ok=True)

        with open("embeddings/embeddings.pkl", "wb") as f:
            pickle.dump(self.database, f)

    def load_database(self):

        with open("embeddings/embeddings.pkl", "rb") as f:
            self.database = pickle.load(f)

    def recognize(self, embedding):

        best_name = "Unknown"
        best_score = -1

        for person, embeddings in self.database.items():

            for saved in embeddings:

                score = cosine_similarity(
                    [embedding],
                    [saved]
                )[0][0]

                if score > best_score:

                    best_score = score
                    best_name = person

        if best_score < 0.5:
            best_name = "Unknown"

        return best_name, best_score