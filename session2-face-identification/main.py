import cv2
import face_recognition
import numpy as np
import os
import io
from PIL import Image

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from GUI import Ui_MainWindow

import mysql.connector
from mysql.connector import Error

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        # Tab 1
        self.t1_org_img_path = 'images/t1/1.jpg' 
        self.t1_up_img_path = None

        self.ui.t1_org_img.setPixmap(QPixmap(self.t1_org_img_path))
        self.ui.t1_pb_load.clicked.connect(self.load_image_tab1)
        self.ui.t1_pb_check.clicked.connect(self.display_message)

        # Tab 2
        self.t2_up_img_path = None
        self.ui.t2_pb_load.clicked.connect(self.load_image_tab2)
        self.ui.t2_pb_match.clicked.connect(self.recognize_faces)

    def load_image_tab1(self):
        image_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', 'images/t1/', "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if image_path:
            self.t1_up_img_path = image_path  # Store the uploaded image path
            self.ui.t1_up_img.setPixmap(QPixmap(image_path))

    def load_image_tab2(self):
        image_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', 'images/t2/', "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if image_path:
            self.t2_up_img_path = image_path  # Store the uploaded image path
            self.ui.t2_up_img.setPixmap(QPixmap(image_path))
            
    def encode_face(self, image_path):
        image = face_recognition.load_image_file(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            return face_encodings[0]
        else:
            return None
    
    def verify_faces(self, t1_org_img_path, t1_up_img_path):
        # Encode faces from both images
        encoding_1 = self.encode_face(t1_org_img_path)
        encoding_2 = self.encode_face(t1_up_img_path)

        if encoding_1 is None or encoding_2 is None:
            return False

        results = face_recognition.compare_faces([encoding_1], encoding_2)
        return results[0]
    
    def display_message(self):
        if self.t1_up_img_path:  # Check if an image has been uploaded
            result = self.verify_faces(self.t1_org_img_path, self.t1_up_img_path)

            message = "Match ✅" if result else "Not a match ❌"
            self.ui.t1_msg.setText(message)  # Update the label with the message
        else:
            QMessageBox.warning(self, "Warning", "Please load an image first 😐.")  # Inform the user that no image is loaded

    def recognize_faces(self):
        if not self.t2_up_img_path:
            QMessageBox.warning(self, "Warning", "Please load an image first 😐.")
            return

        # Load known face encodings from the database
        known_face_encodings, known_face_names = self.load_known_faces_from_db()

        # Load the image
        image = face_recognition.load_image_file(self.t2_up_img_path)
        
        # Find all face locations and face encodings in the image
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        # Loop through each face found in the unknown image
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # Draw a box around the face
            cv2.rectangle(image, (left, top), (right, bottom), (0, 85, 255, 220), 2)

            # Draw a label with a name below the face
            cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 85, 255, 220), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
            
        # Convert the image to Qt format
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        
        # Display the result
        self.ui.t2_up_img.setPixmap(QPixmap.fromImage(qImg))

    def load_known_faces_from_db(self):
        known_face_encodings = []
        known_face_names = []

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="my_user",
                password="my_password",
                database="images_db"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT image_name, image_column FROM images_store")
            results = cursor.fetchall()

            for name, image_data in results:
                # Convert image data to numpy array
                nparr = np.frombuffer(image_data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                # Get face encoding
                face_encoding = face_recognition.face_encodings(img)[0]
                
                known_face_encodings.append(face_encoding)
                known_face_names.append(os.path.splitext(name)[0])

            cursor.close()
            conn.close()

        except Error as e:
            print(f"Error accessing database: {e}")

        return known_face_encodings, known_face_names

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())