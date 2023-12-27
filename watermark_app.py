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


# Функция для загрузки водяного знака
def load_watermark():
    file_path = filedialog.askopenfilename()
    if file_path:
        watermark = Image.open(file_path)
        global base_image
        watermarked_image = base_image.copy()
        watermark = watermark.convert("RGBA")
        width, height = base_image.size
        # Регулировка размера водяного знака
        watermark = watermark.resize((width // 2, watermark.size[1] * width // 2 // watermark.size[0]))
        # Размещение водяного знака по центру изображения
        watermark_width, watermark_height = watermark.size
        position = ((width - watermark_width) // 2, (height - watermark_height) // 2)
        watermarked_image.paste(watermark, position, watermark)

        photo = ImageTk.PhotoImage(watermarked_image)
        image_label.config(image=photo)
        image_label.image = photo
        global result_image
        result_image = watermarked_image


# Функция для сохранения результата
def save_result():
    if result_image is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            result_image.save(file_path)

 # Создание графического интерфейса
app = tk.Tk()
app.title("Добавить водяной знак")
app.geometry("600x400")

load_image_button = tk.Button(app, text="Загрузить фотографию", command=load_image)
load_image_button.pack()

load_watermark_button = tk.Button(app, text="Загрузить водяной знак", command=load_watermark)
load_watermark_button.pack()

save_button = tk.Button(app, text="Сохранить результат", command=save_result)
save_button.pack()

image_label = tk.Label(app)
image_label.pack()

base_image = None
result_image = None

app.mainloop()
