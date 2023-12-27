import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Функция для загрузки фотографии
def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        global base_image
        base_image = image


