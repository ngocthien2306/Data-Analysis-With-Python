from deepface import DeepFace
result = DeepFace.verify(img1_path = "images/yoona.jpg", img2_path = "images/yoona1.jpg")
print(result)