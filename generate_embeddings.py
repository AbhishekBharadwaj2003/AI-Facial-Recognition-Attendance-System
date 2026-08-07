from utils.recognizer import FaceRecognizer

recognizer = FaceRecognizer()

recognizer.generate_embeddings()

recognizer.save_database()

print("Embeddings Generated Successfully")