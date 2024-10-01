from deepface import DeepFace
backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'fastmtcnn',
  'retinaface', 
  'mediapipe',
  'yolov8',
  'yunet',
  'centerface',
]

alignment_modes = [True, False]

#face verification
obj = DeepFace.verify(
  img1_path = "1.jpg", 
  img2_path = "2.jpg", 
  detector_backend = backends[2],
  align = alignment_modes[1],
)

print(obj)