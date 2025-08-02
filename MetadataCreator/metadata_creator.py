import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import json
import sqlite3
import google.generativeai as genai

class MetadataCreator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Metadata Creator")
        self.geometry("800x600")

        self.db_conn = sqlite3.connect('C:\\dev\\Piculator\\db\\piculator.db')

        self.api_key_entry = tk.Entry(self, width=50, show="*")
        self.api_key_entry.pack(pady=5)
        self.api_key_entry.insert(0, "AIzaSyBxVyDDVN7dftzNav-bRli9ikaSiJ9FcoA")

        self.btn_browse = tk.Button(self, text="Browse Images", command=self.browse_images)
        self.btn_browse.pack(pady=10)

        self.preview_frame = tk.Frame(self)
        self.preview_frame.pack(fill="both", expand=True)

        self.btn_extract = tk.Button(self, text="Extract Metadata", command=self.extract_metadata)
        self.btn_extract.pack(pady=10)

        self.metadata_text = tk.Text(self, height=10)
        self.metadata_text.pack(pady=10)

        self.selected_files = []

    def browse_images(self):
        filepaths = filedialog.askopenfilenames(
            initialdir="C:\\dev\\Piculator\\portfolio",
            title="Select Images",
            filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*"))
        )
        self.selected_files = filepaths

        for widget in self.preview_frame.winfo_children():
            widget.destroy()

        for filepath in filepaths:
            self.show_preview(filepath)

    def show_preview(self, filepath):
        try:
            img = Image.open(filepath)
            img.thumbnail((150, 150))
            img_tk = ImageTk.PhotoImage(img)

            panel = tk.Label(self.preview_frame, image=img_tk)
            panel.image = img_tk
            panel.pack(side="left", padx=10, pady=10)
        except Exception as e:
            print(f"Error opening {filepath}: {e}")

    def extract_metadata(self):
        self.metadata_text.delete("1.0", tk.END)
        api_key = self.api_key_entry.get()
        if not api_key or api_key == "Enter your Gemini API Key":
            self.metadata_text.insert(tk.END, "Please enter a valid Gemini API Key.")
            return

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro-vision')

        for filepath in self.selected_files:
            try:
                img = Image.open(filepath)
                response = model.generate_content(["Extract metadata from this image.", img], stream=True)
                response.resolve()

                metadata = self.parse_gemini_response(response.text)
                self.save_to_db(filepath, metadata)
                self.metadata_text.insert(tk.END, f"--- {os.path.basename(filepath)} ---\n")
                self.metadata_text.insert(tk.END, json.dumps(metadata, indent=2))
                self.metadata_text.insert(tk.END, "\n\n")
            except Exception as e:
                self.metadata_text.insert(tk.END, f"Error processing {os.path.basename(filepath)}: {e}\n\n")

    def parse_gemini_response(self, response_text):
        # This is a simple parser. A more robust implementation would be needed for production.
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            return {"description": response_text}

    def save_to_db(self, filepath, metadata):
        c = self.db_conn.cursor()
        c.execute("INSERT INTO images (filename, filepath, metadata, style, source_model) VALUES (?, ?, ?, ?, ?)",
                    (os.path.basename(filepath), filepath, json.dumps(metadata), metadata.get('style'), 'mock_gemini'))
        self.db_conn.commit()

    def __del__(self):
        self.db_conn.close()

if __name__ == "__main__":
    app = MetadataCreator()
    app.mainloop()