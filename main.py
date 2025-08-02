import tkinter as tk

class AppLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Piculator Launcher")
        self.geometry("300x200")

        self.btn_metadata = tk.Button(self, text="Launch Metadata Creator", command=self.launch_metadata_creator)
        self.btn_metadata.pack(pady=20)

        self.btn_image = tk.Button(self, text="Launch Image Creator", command=self.launch_image_creator)
        self.btn_image.pack(pady=20)

    def launch_metadata_creator(self):
        self.destroy()
        os.system("python C:\\dev\\Piculator\\MetadataCreator\\metadata_creator.py")

    def launch_image_creator(self):
        self.destroy()
        os.system("python C:\\dev\\Piculator\\ImageCreator\\image_creator.py")

if __name__ == "__main__":
    import os
    app = AppLauncher()
    app.mainloop()
