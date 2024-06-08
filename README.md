# Image Editor

This project is a simple image editor built with Python's Tkinter library and the Python Imaging Library (PIL). The editor allows users to open, edit, and save images with various functionalities including drawing, cropping, rotating, adding text, and applying filters.

## Features

- **Open Image:** Load JPEG or PNG images into the editor.
- **Save Image:** Save the edited image in PNG or JPEG format.
- **Draw:** Draw on the image with a configurable pen size and color.
- **Crop:** Select and crop a portion of the image.
- **Rotate:** Rotate the image 90 degrees counterclockwise.
- **Add Text:** Add custom text to the image.
- **Filters:** Apply various filters such as Black and White, Blur, Sharpen, Smooth, Emboss, Contour, Edge Enhance, and Detail.
- **Clear Canvas:** Reset the image to its original state before modifications.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/image-editor.git
    cd image-editor
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python image_editor.py
    ```

## Dependencies

- Python 3.x
- Tkinter (comes pre-installed with Python)
- Pillow

You can install Pillow using:
```sh
pip install Pillow
```

## Usage

1. **Open Image:** Click on "Add Image" button to load an image.
2. **Draw:** Click on "Draw" button, then use the mouse to draw on the image. Adjust the pen size and color using the respective options.
3. **Crop:** Click on "Crop" button, draw a rectangle on the image, and release to crop the selected area.
4. **Rotate:** Click on "Rotate" button to rotate the image 90 degrees counterclockwise.
5. **Add Text:** Click on "Add Text" button, draw a rectangle to define text area, enter the text, and choose font color.
6. **Filters:** Click on "Select a filter" button, choose a filter from the menu, and apply it to the image.
7. **Clear Canvas:** Click on "Clear" button to revert the image to its original state.
8. **Save Image:** Click on "Save" button to save the edited image.

## Screenshots

<img width="1112" alt="Ekran Resmi 2024-06-08 18 34 02" src="https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/ef2ae46c-dea1-44f7-941b-6dd30591d79d">

<img width="1112" alt="Ekran Resmi 2024-06-08 18 34 39" src="https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/0a50c83d-1a2c-45fb-9dd8-46bc156ef9b2">

<img width="1112" alt="Ekran Resmi 2024-06-08 18 35 18" src="https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/be1ed2cf-fc49-45e9-927a-5ac4f0d402d6">

<img width="1112" alt="Ekran Resmi 2024-06-08 18 36 03" src="https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/d1cbd10a-7e68-4002-9a78-069630c7aecc">








