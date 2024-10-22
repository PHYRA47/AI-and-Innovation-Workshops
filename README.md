# 🤖 AI and Innovation Workshop

Welcome to the **AI and Innovation Workshop** course repository! This repository contains assignments from the 3rd semester course of my Master's in Photonics for Security, Reliability, and Safety (PSRS) at UPEC University, Paris Est-Créteil.

Each session has its own unique project, where we build exciting applications using Python, PyQt5, and AI models. 🚀

## 📝 Assignments Overview

### 1️⃣ Session 1: Face Verification
- **Task**: Develop a face verification app.
- **Instructions**: 
    - Load an image and match it with a base image.
    - Display both images side by side.
    - Show a message if the faces match. 🎉

### 2️⃣ Session 2: Face Recognition and Database Integration
- **Task**: Extend the face verification app to include face recognition.
- **Instructions**:
    - Add a second tab in the GUI for face recognition.
    - Use a database to match the face (not local files).
    - Display the recognized face with a bounding box and name, or `UNKNOWN` if no match. 🧑‍💻

### 3️⃣ Session 3: LLM Chat GUI
- **Task**: Create a chat interface for a Large Language Model (LLM).
- **Instructions**:
    - Host the LLM API on Colab using Ngrok for public access.
    - Build a simple GUI to chat with the LLM and display responses. 🧠💬
 
### 4️⃣ Session 4: Multi-Modal LLMs
- **Task**: Create a multi-modal LLM app with text and image input.
- **Instructions**:
    - Host the [**openbmb/MiniCPM-V-2_6-int4**](https://huggingface.co/openbmb/MiniCPM-V-2_6-int4) model API on Colab using ngrok for public access.
    - Create two POST routes:
        - **Route 1**: Send a text prompt via a POST request and get a response from the LLM. 📝➡️🤖
        - **Route 2**: Send a text prompt + image, and receive a response from the LLM. 🖼️➕📝➡️🤖
    - Build a GUI to utilize these routes and interact with the model.


## 🛠️ Technologies Used
- **Language**: Python 🐍
- **GUI Framework**: PyQt5 🖥️
- **API Hosting**: Colab + Ngrok 🌐
- **Face Recognition**: OpenCV and custom models 📸
- **LLM Model**: openbmb/MiniCPM-V-2_6-int4 🤖
- **Multi-modal Processing**: Text + Image inputs for LLM responses 📝🖼️

## 📂 Repository Structure
- Each session's project is stored in its respective folder with the code and resources.
- Feel free to explore the individual assignments! 😎

