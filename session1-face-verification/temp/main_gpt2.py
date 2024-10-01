from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QLabel to display the message
        self.messageLabel = QLabel(self)
        
        # Create a QPushButton
        self.button = QPushButton('Click Me', self)
        
        # Connect the button's clicked signal to the update_label function
        self.button.clicked.connect(self.update_label)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.messageLabel)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # Set the window title and size
        self.setWindowTitle('Display Message Example')
        self.setGeometry(100, 100, 300, 200)

    def update_label(self):
        # This function updates the label's text
        message = self.get_message()  # Call your function to get the message
        self.messageLabel.setText(message)  # Update the label with the message

    def get_message(self):
        # Example function that returns a message
        return "Hello, this is your message!"

# Run the application
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
