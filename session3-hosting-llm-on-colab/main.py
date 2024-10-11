from PyQt5.QtWidgets import QMainWindow, QApplication
from GUI3 import Ui_MainWindow
import requests

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
   
        self.ui.pushButton.clicked.connect(self.get_model_response)
        self.chat_history = []

    def get_model_response(self):
        user_input = self.ui.input_txt.text()
        self.chat_history.append(f"User: {user_input}")
        
        headers = {"Content-Type": "application/json"}
        base_url = "https://7663-35-185-179-76.ngrok-free.app"  # Update this with your actual base URL
        endpoint = f"{base_url}/generate"
        
        response = requests.post(endpoint, headers=headers, json={
            "inputs": "\n\n### Instructions:\n" + user_input + "\n\n### Response:\n",
            "parameters": {"stop": ["\n", "###"]}
        })
        
        output = response.json()
        llm_response = output.get("generated_text", "No Response Found")
        self.chat_history.append(f"LLM: {llm_response}")
        
        self.update_chat_display()
        self.ui.input_txt.clear() # clears the text from the input field 

    def update_chat_display(self):
        chat_display = "\n\n".join(self.chat_history)
        self.ui.output_txt.setText(chat_display)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())