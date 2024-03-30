import os
import shutil
from PIL import Image, ExifTags, ImageTk
import tkinter as tk

class PhotoSelector:

    def __init__(self, source_folder, selected_folder, skipped_folder):
        self.source_folder = source_folder
        self.selected_folder = selected_folder
        self.skipped_folder = skipped_folder
        self.files = os.listdir(source_folder)
        self.current_index = 0
        
        self.selected_photos = os.listdir(selected_folder)
        self.skipped_photos = os.listdir(skipped_folder)

        self.root = tk.Tk()
        self.root.title("Photo Selector")
        self.root.geometry("1920x1080")  # Set the window size to match your screen resolution
        
        self.label = tk.Label(self.root)
        self.label.pack(expand=True, fill="both")
        
        self.root.bind('<Left>', self.prev_photo)
        self.root.bind('<Right>', self.next_photo)
        self.root.bind('y', self.select_photo)
        self.root.bind('n', self.skip_photo)
        self.root.bind('c', self.quit_app)
        
        self.load_image()

        self.root.mainloop()

    def load_image(self):
        file_name = self.files[self.current_index]
        
        if file_name in self.selected_photos or file_name in self.skipped_photos:
            self.next_photo()
            return

        image_path = os.path.join(self.source_folder, file_name)
        try:
            img = Image.open(image_path)
            remaining = len(self.files) - (len(self.selected_photos) + len(self.skipped_photos))
            self.root.title(f"{file_name} - {len(self.selected_photos)} selected - {len(self.skipped_photos)} skipped - {remaining} remaining")
            # Check for image orientation and rotate if necessary
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(img._getexif().items())

            if exif[orientation] == 3:
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 6:
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 8:
                img = img.rotate(90, expand=True)
            
            # Resize the image to fit the screen
            img.thumbnail((1920, 1080))
            
            self.photo = ImageTk.PhotoImage(img)
            self.label.config(image=self.photo)
        except Exception as e:
            print(f"Unable to open image '{file_name}': {e}")
            self.next_photo()

    def select_photo(self, event=None):
        file_name = self.files[self.current_index]
        source_path = os.path.join(self.source_folder, file_name)
        destination_path = os.path.join(self.selected_folder, file_name)
        shutil.copyfile(source_path, destination_path)
        print(f"Photo '{file_name}' copied to '{self.selected_folder}'.")
        self.selected_photos.append(file_name)
        self.next_photo()

    def skip_photo(self, event=None):
        file_name = self.files[self.current_index]
        source_path = os.path.join(self.source_folder, file_name)
        skip_path = os.path.join(self.skipped_folder, file_name)
        shutil.copyfile(source_path, skip_path)
        print(f"Photo '{file_name}' copied to '{self.skipped_folder}'.")
        self.skipped_photos.append(file_name)
        self.next_photo()

    def next_photo(self, event=None):
        self.current_index += 1
        if len(self.selected_photos) + len(self.skipped_photos) >= len(self.files):
            print("Selection process completed.")
            self.root.destroy()
            return
        file_name = self.files[self.current_index]
     
        if not file_name.endswith(".jpg") or file_name in self.selected_photos or file_name in self.skipped_photos:
            self.next_photo()
            return
       
        self.load_image()

    def prev_photo(self, event=None):
        self.current_index -= 1
        
        file_name = self.files[self.current_index]
       
        if not file_name.endswith(".jpg") or file_name in self.selected_photos or file_name in self.skipped_photos:
            self.prev_photo()
            return
      
        self.load_image()
        
        
    def quit_app(self, event=None):
        self.root.destroy()
        return
        
        
# Replace these paths with your source folder and destination subfolder paths
source_folder = "REPLACE WITH PATH OF YOUR FOLDER WITH PHOTOS"
selected_folder = os.path.join(source_folder, "selected")
skipped_folder = os.path.join(source_folder, "skipped")

PhotoSelector(source_folder, selected_folder, skipped_folder)
