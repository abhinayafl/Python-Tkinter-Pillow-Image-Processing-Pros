from tkinter import Tk, Button, Canvas, filedialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter App")

        self.image_path = None
        self.original_image = None
        self.filtered_image = None

        self.create_widgets()

    def create_widgets(self):
        # Canvas untuk menampilkan gambar
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack(side="top", pady=5)

        # Dropdown (Combobox) untuk memilih filter
        self.filter_combobox = ttk.Combobox(self.root, values=["Blur", "Grayscale", "Sharpness", "Edge Enhance", "Emboss", "Contour"])
        self.filter_combobox.set("Select Filter")
        self.filter_combobox.pack(side="top", pady=5)

        # Frame untuk menyusun tombol-tombol secara horizontal
        button_frame = ttk.Frame(self.root)
        button_frame.pack(side="bottom", pady=5)

        # Button untuk mengunggah gambar
        self.upload_button = Button(button_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(side="left", padx=5)

        # Button untuk menerapkan filter
        self.apply_button = Button(button_frame, text="Apply Filter", command=self.apply_selected_filter)
        self.apply_button.pack(side="left", padx=5)

        # Button untuk menyimpan gambar
        self.save_button = Button(button_frame, text="Save Image", command=self.save_image)
        self.save_button.pack(side="left", padx=5)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.display_image(self.original_image)

    def display_image(self, image):
        image.thumbnail((400, 400))
        self.photo_image = ImageTk.PhotoImage(image)
        self.canvas.config(width=self.photo_image.width(), height=self.photo_image.height())
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)

    def apply_selected_filter(self):
        filter_name = self.filter_combobox.get()
        if filter_name and self.original_image:
            if filter_name == "Blur":
                self.filtered_image = self.original_image.filter(ImageFilter.BLUR)
            elif filter_name == "Grayscale":
                self.filtered_image = self.original_image.convert("L") #luminance 
            elif filter_name == "Sharpness":
                self.filtered_image = self.original_image.filter(ImageFilter.SHARPEN)
            elif filter_name == "Edge Enhance":
                self.filtered_image = self.original_image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter_name == "Emboss":
                self.filtered_image = self.original_image.filter(ImageFilter.EMBOSS)
            elif filter_name == "Contour":
                self.filtered_image = self.original_image.filter(ImageFilter.CONTOUR)

            self.display_image(self.filtered_image)

    def save_image(self):
        if self.filtered_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                self.filtered_image.save(save_path)

if __name__ == "__main__":
    root = Tk()
    app = ImageFilterApp(root)
    root.mainloop()
