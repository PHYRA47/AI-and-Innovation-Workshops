import cv2
import face_recognition
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from GUI import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self) 

        # Connect the Load Image button to the load_image method
        self.pb_load.clicked.connect(self.load_image)

        # Create a QLabel to display the image in the original_img widget
        self.original_image_label = QLabel(self.orginal_img)
        layout = QVBoxLayout(self.orginal_img)
        layout.addWidget(self.original_image_label)
        self.original_image_label.setAlignment(Qt.AlignCenter)
    
    def load_image(self):
        # Open file dialog to select an image file
        image_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', "Image Files (*.png *.jpg *.jpeg *.bmp)")

        if image_path:
            # Load the image using cv2
            image = cv2.imread(image_path)

            # Convert the image to RGB format
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Convert the image to QImage format
            height, width, channels = image.shape
            bytes_per_line = channels * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Convert QImage to QPixmap and display it in the QLabel
            pixmap = QPixmap.fromImage(q_image)
            self.original_image_label.setPixmap(pixmap)
            self.original_image_label.setScaledContents(True)  # Make the image fit within the label

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
