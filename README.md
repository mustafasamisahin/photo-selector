# Photo Selector App

The Photo Selector app is a simple Python application that allows users to browse through a folder of images and selectively copy them to different subfolders based on their selection.

## Features

- Browse through a folder of images one by one.
- Select images to copy to a "selected" subfolder.
- Skip images to copy them to a "skipped" subfolder.
- Navigate through images using keyboard arrow keys.
- Full-screen image viewing.

## Requirements

- Python 3.x
- tkinter (Included in standard Python library)
- Pillow (Python Imaging Library)

## Usage

1. Clone or download the repository to your local machine.
2. Install the required Python packages:
```
pip install Pillow
```
4. Open a terminal or command prompt and navigate to the directory containing the `photo_selector.py` file.
5. Run the script by executing the following command:
```
python photo_selector.py
```
6. The app window will open, displaying the first image in the folder.
7. Use the following keyboard shortcuts:
- Left Arrow: Previous image
- Right Arrow: Next image
- 'y': Select current image
- 'n': Skip current image
- 'c': Close the app
7. Once you've finished selecting images, close the app window to exit.

## Folder Structure

The app assumes the following folder structure:
- Source folder: Contains the original images to be selected from.
- Selected folder: Images selected by the user will be copied to this folder.
- Skipped folder: Images skipped by the user will be copied to this folder.

Make sure to adjust the folder paths in the `photo_selector.py` file according to your directory structure.

## Notes

- Supported image formats: JPEG, PNG, GIF, BMP, TIFF.
- Image rotation is supported based on EXIF metadata.
- Images are resized to fit the screen resolution (1920x1080).

