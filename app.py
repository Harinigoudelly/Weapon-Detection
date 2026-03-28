import streamlit as st
from PIL import Image
import numpy as np
import cv2
import tempfile
from model import detect_weapon

st.title("🔫 Weapon Detection (Faster R-CNN)")

option = st.radio("Choose Input", ["Image", "Video"])

# ---------- IMAGE ---------- #
if option == "Image":
    file = st.file_uploader("Upload Image", type=["jpg","png"])

    if file:
        image = Image.open(file)
        img = np.array(image)

        boxes, scores = detect_weapon(image)

        for box, score in zip(boxes, scores):
            x1, y1, x2, y2 = box
            cv2.rectangle(img, (x1,y1),(x2,y2),(255,0,0),2)
            cv2.putText(img, f"Weapon {score*100:.1f}%",
                        (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,(255,0,0),2)

        st.image(img, caption="Result")

# ---------- VIDEO ---------- #
elif option == "Video":
    file = st.file_uploader("Upload Video", type=["mp4"])

    if file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())

        cap = cv2.VideoCapture(tfile.name)
        frame_window = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            boxes, scores = detect_weapon(image)

            for box, score in zip(boxes, scores):
                x1, y1, x2, y2 = box
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)

            frame_window.image(frame, channels="BGR")

        cap.release()