import face_recognition
import cv2

def load_image(image_path):
    image = face_recognition.load_image_file(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return rgb_image

def encode_face(image_path):
    image = load_image(image_path)
    face_encodings = face_recognition.face_encodings(image)
    if len(face_encodings) > 0:
        return face_encodings[0]
    else:
        return None

def verify_faces(image1_path, image2_path):
    # Encode faces from both images
    encoding_1 = encode_face(image1_path)
    encoding_2 = encode_face(image2_path)

    if encoding_1 is None or encoding_2 is None:
        print("One of the images doesn't contain a detectable face.")
        return False

    # Compare the faces and return True if they match
    results = face_recognition.compare_faces([encoding_1], encoding_2)
    return results[0]

if __name__ == "__main__":
    # Define paths to your input images
    image1 = "1.jpg"
    image2 = "3.jpg"

    # Perform face verification
    if verify_faces(image1, image2):
        print("The faces match!")
    else:
        print("The faces do not match.")