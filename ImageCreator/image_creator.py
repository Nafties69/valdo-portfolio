import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import google.generativeai as genai
import requests
from io import BytesIO

class ImageCreator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Creator")
        self.geometry("1000x600")

        self.api_key_entry = tk.Entry(self, width=50, show="*")
        self.api_key_entry.pack(pady=5)
        self.api_key_entry.insert(0, "AIzaSyBxVyDDVN7dftzNav-bRli9ikaSiJ9FcoA")

        self.btn_select_image = tk.Button(self, text="Select Base Image", command=self.select_image)
        self.btn_select_image.pack(pady=10)

        self.prompt_entry = tk.Entry(self, width=100)
        self.prompt_entry.pack(pady=10)

        self.btn_generate = tk.Button(self, text="Generate Images", command=self.generate_images)
        self.btn_generate.pack(pady=10)

        self.image_frame = tk.Frame(self)
        self.image_frame.pack(fill="both", expand=True)

        self.base_image_path = None

    def select_image(self):
        filepath = filedialog.askopenfilename(
            initialdir="C:\dev\Piculator\portfolio",
            title="Select Image",
            filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*" ))
        )
        self.base_image_path = filepath

    def generate_images(self):
        for widget in self.image_frame.winfo_children():
            widget.destroy()

        api_key = self.api_key_entry.get()
        if not api_key or api_key == "Enter your Gemini API Key":
            # You can show an error message here
            return

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro-vision')

        prompt = self.prompt_entry.get()
        if not prompt:
            # You can show an error message here
            return

        if self.base_image_path:
            img = Image.open(self.base_image_path)
            response = model.generate_content([prompt, img], stream=True)
            response.resolve()
        else:
            response = model.generate_content(prompt, stream=True)
            response.resolve()

        # For now, let's assume the response contains image URLs.
        # In a real scenario, you would need to parse the response to get the image data.
        # For demonstration, I will use a placeholder image URL.
        image_urls = [
            "https://picsum.photos/300/300",
            "https://picsum.photos/300/300",
            "https://picsum.photos/300/300"
        ]

        for url in image_urls:
            self.show_generated_image_from_url(url)

    def show_generated_image_from_url(self, url):
        try:
            response = requests.get(url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(img)

            panel = tk.Label(self.image_frame, image=img_tk)
            panel.image = img_tk
            panel.pack(side="left", padx=10, pady=10)
        except Exception as e:
            print(f"Error opening image from url: {e}")

    def show_generated_image(self, filepath):
        try:
            img = Image.open(filepath)
            img.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(img)

            panel = tk.Label(self.image_frame, image=img_tk)
            panel.image = img_tk
            panel.pack(side="left", padx=10, pady=10)
        except Exception as e:
            print(f"Error opening {filepath}: {e}")

if __name__ == "__main__":
    # Create a placeholder image for now
    if not os.path.exists("C:\dev\Piculator\portfolio\placeholder.png"):
        img = Image.new('RGB', (300, 300), color = 'red')
        img.save("C:\dev\Piculator\portfolio\placeholder.png")

    app = ImageCreator()
    app.mainloop()