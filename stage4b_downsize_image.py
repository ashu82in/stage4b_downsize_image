#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:09:31 2024

@author: ashutoshgoenka
"""

import streamlit as st
from PIL import Image
import PIL
import os
import zipfile
from zipfile import ZipFile, ZIP_DEFLATED
import pathlib
import shutil


try:
    shutil.rmtree("images_comp_resized")
except:
    pass


try:
    os.mkdir("images_comp_resized")
except:
    pass


def resize(img, new_width):
    width, height  = img.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = img.resize((new_width, new_height), resample=PIL.Image.LANCZOS)
    return resized_image



st.title("Stage 4B - Downsize Images")
# st.write('My first app Hello *world!*')
up_files = st.file_uploader("Upload Image Files", type = ["png", "jpeg", "jpg"] ,accept_multiple_files=True)
# st.write(up_files)


for file in up_files:
    extensions = ["jpg", "jpeg", "png", "gif", "webp"]
    im = Image.open(file)
    ext = file.name.split(".")[-1]
    im_resized = resize(im, 900)
    im_resized.save("images_comp_resized/"+file.name)
    
zip_path = "images_compressed_downsized.zip"
directory_to_zip = "images_comp_resized"
folder = pathlib.Path(directory_to_zip)
# st.write(folder)


with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zip:
    for file in folder.iterdir():
        zip.write(file, arcname=file.name)
        
with open("images_compressed_downsized.zip", "rb") as fp:
    btn = st.download_button(
        label="Download ZIP",
        data=fp,
        file_name="images_compressed_downsized.zip",
        mime="application/zip"
    )
    