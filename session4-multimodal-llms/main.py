from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication
from PyQt5.QtGui import QPixmap
from GUI import Ui_MainWindow

import requests
import json

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # fist tab
        self.ui.t1_pb_send.clicked.connect(self.text_to_model)
        self.chat_history = []
        
        # second tab
        self.ui.t2_pb_upload.clicked.connect(self.upload_image)
        self.ui.t2_pb_send.clicked.connect(self.text_and_image_to_model)

        self.base_url = "https://a941-34-169-32-250.ngrok-free.app"
        self.t2_uploaded_image_path = None

    def text_to_model(self):

        user_input = self.ui.t1_input_txt.text()
        if not user_input:
                QMessageBox.warning(self, "Input Error", "Please enter a prompt.")
                return
        
        self.chat_history.append(f"User: {user_input}")

        headers = {"Content-Type": "application/json"}
        endpoint = f"{self.base_url}/generate_text"
        
        data = {"inputs": user_input}
        response = requests.post(endpoint, headers=headers, json=data)
        
        result = response.json()
        llm_response = result.get("generated_text", "No text generated")
        self.ui.t1_output_txt.setText(llm_response)
        self.chat_history.append(f"LLM: {llm_response}")

        self.update_chat_display()
        self.ui.t1_input_txt.clear()

    def update_chat_display(self):
        chat_display = "\n\n".join(self.chat_history)
        self.ui.t1_output_txt.setText(chat_display)

    def upload_image(self):
        image_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', 'images/', "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if image_path:
            self.t2_uploaded_image_path = image_path  # Store the uploaded image path
            self.ui.t2_uploaded_img.setPixmap(QPixmap(image_path))

    """
    from PyQt5.QtCore import Qt

    def upload_image(self):
    image_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', 'images/', "Image Files (*.png *.jpg *.jpeg *.bmp)")
    if image_path:
        # Load the image
        pixmap = QPixmap(image_path)

        # Get the size of the label to scale the pixmap to fit within it
        label_size = self.ui.t2_uploaded_img.size()

        # Scale the pixmap while keeping the aspect ratio
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Set the scaled pixmap to the QLabel
        self.ui.t2_uploaded_img.setPixmap(scaled_pixmap)
    """
# """
    def text_and_image_to_model(self):
            if not self.t2_uploaded_image_path:
                QMessageBox.warning(self, "Input Error", "Please upload an image first.")
                return

            user_input = self.ui.t2_input_txt.text()
            if not user_input:
                QMessageBox.warning(self, "Input Error", "Please enter a prompt.")
                return

            endpoint = f"{self.base_url}/generate_text_image"
            
            try:
                with open(self.t2_uploaded_image_path, 'rb') as image_file:
                    files = {'file': image_file}
                    data = {'prompt': user_input}
                    response = requests.post(endpoint, files=files, data=data)
                    response.raise_for_status()
                    result = response.json()
                    self.ui.t2_output_txt.setText(result.get("generated_text", "No text generated"))
            except requests.RequestException as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
# """
"""
    def text_and_image_to_model(self):
        if self.uploaded_image_path and self.t2_input_txt.text():
                endpoint = f"{self.base_url}/generate_text_image"
                
                with open(self.t2_uploaded_image_path, 'rb') as image_file:
                    files = {'file': image_file}
                    data = {'prompt': self.t2_input_txt.text()}
                    response = requests.post(endpoint, files=files, data=data)
                    
                    if response.status_code == 200:
                        result = response.json()
                        self.t2_output_txt.setText(result.get("generated_text", "No text generated"))
                    else:
                        self.t2_output_txt.setText("Error in API response")
"""
                        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
