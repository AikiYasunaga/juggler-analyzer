import cv2
import numpy as np
import streamlit as st
from PIL import Image

def get_last_value(img):

    img = np.array(img)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([20,100,100])
    upper = np.array([35,255,255])

    mask = cv2.inRange(hsv, lower, upper)

    coords = np.column_stack(np.where(mask > 0))

    if len(coords) == 0:
        return None

    last_point = coords[coords[:,1].argmax()]

    y = last_point[0]

    height = img.shape[0]

    value = (1 - y/height) * 10000 - 5000

    return int(value)


st.title("ジャグラースランプグラフ解析")

file = st.file_uploader("画像アップロード")

if file:

    image = Image.open(file)

    st.image(image)

    result = get_last_value(image)

    if result:
        st.write("最終差枚:",result,"枚")
    else:
        st.write("解析できませんでした")
