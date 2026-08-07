import sys

from utils.student_registration import StudentRegistrar
from utils.recognizer import FaceRecognizer

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Enter Student Name : ")

registrar = StudentRegistrar()

registrar.register(name)

recognizer = FaceRecognizer()

recognizer.generate_embeddings()

recognizer.save_database()

print("Student Registered Successfully.")