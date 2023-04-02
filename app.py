import streamlit as st
from model import predict_image


st.write("""
         # Predict Retina Damage From Optical Coherence Tomography (OCT)
         """
         )
st.write("This is a simple image classification web app to predict retina damage")
file = st.file_uploader("Please upload an image file", type=["jpeg", "jpg", "png"], accept_multiple_files=True)
images = {img.name: predict_image(img) for img in file}

answer = 0
for key, value in images.items():
    folder = key.split("-")[0]
    answer += 1 if value == folder else 0

if images:
    st.write(f"Image(s): {images}")
    st.write(f"Predicted value: {(answer / len(images)) * 100}%")



