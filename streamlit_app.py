import streamlit as st
import cv2
import numpy as np

st.title('Portrait Mode OpenCV')

import streamlit as st
from PIL import Image
st.set_option('deprecation.showfileUploaderEncoding', False)

# Upload an image and set some options for demo purposes
st.header("Cropper Demo")
img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg'])
realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
aspect_dict = {
    "1:1": (1, 1),
    "16:9": (16, 9),
    "4:3": (4, 3),
    "2:3": (2, 3),
    "Free": None
}

Bright_value = st.slider("Bright", min_value=0.5, max_value=3.5)
Blurr_value = st.slider("Blurr", min_value=0.5, max_value=3.5)

aspect_ratio = aspect_dict[aspect_choice]

if img_file:
    img = Image.open(img_file)
    if not realtime_update:
        st.write("Double click to save crop")
    # Get a cropped image from the frontend
    cropped_img = img
    # Manipulate cropped image at will
    st.write("Preview")
    _ = cropped_img.thumbnail((300,300))
    st.image(cropped_img)