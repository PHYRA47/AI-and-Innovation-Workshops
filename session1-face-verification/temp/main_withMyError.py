import cv2
import face_recognition
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from GUI import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        # Load first image (original Image)
        self.original_img_path = '1.jpg'
        pixmap = QPixmap(self.original_img_path)
        self.ui.original_img.setPixmap(pixmap)

        # Connect the Load Image button to the load_image method
        self.ui.pb_load.clicked.connect(self.load_image)

        # Connect the check button to the display_message function
        self.ui.pb_check.clicked.connect(self.display_message)

    def load_image(self):
        uploaded_image_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if uploaded_image_path:
            self.ui.uploaded_img.setPixmap(QPixmap(uploaded_image_path))
            return uploaded_image_path  # Return the path of the uploaded image
            
    def encode_face(self, image_path):
        image = face_recognition.load_image_file(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            return face_encodings[0]
        else:
            return None
    
    def verify_faces(self, original_img_path, uploaded_img_path):
        # Encode faces from both images
        encoding_1 = self.encode_face(original_img_path)
        encoding_2 = self.encode_face(uploaded_img_path)

        if encoding_1 is None or encoding_2 is None:
            return False

        results = face_recognition.compare_faces([encoding_1], encoding_2)
        return results[0]
    
    def display_message(self):
        uploaded_image_path = self.load_image()  # Get the uploaded image path
        if uploaded_image_path:  # Ensure the image was loaded
            result = self.verify_faces(self.original_img_path, uploaded_image_path)

            message = "✅" if result else "❌"
            self.ui.l_message.setText(message)  # Update the label with the message

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
