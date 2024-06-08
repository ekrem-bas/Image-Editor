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
    git clone https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project.git
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

![1](https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/094865b0-e7cb-4ac8-a7b2-e2911f77bd1e)

![2](https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/1173752f-fb89-4cd4-8e12-fa8a8e70f015)

![3](https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/4e64a303-8d8f-4a43-b029-e92b572ded81)

![4](https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/b1f37c91-887a-45ad-911a-a68eb4ecd06c)
