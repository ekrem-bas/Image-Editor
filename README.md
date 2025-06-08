# Python Image Editor

A user-friendly desktop image editing application built with Python, Tkinter, and the Pillow library. This application provides a simple graphical user interface to perform essential image editing operations, including drawing, cropping, rotating, adding text, and applying a variety of artistic filters.

![Screenshot of the Image Editor](https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/094865b0-e7cb-4ac8-a7b2-e2911f77bd1e)

## Key Features

-   **File Operations**: Open JPEG and PNG image files. Save the final edited image back to your disk in either PNG or JPEG format.
-   **Drawing Tools**: Engage a freehand drawing mode to draw directly on the image. You can customize the pen size and color.
-   **Image Transformation**:
    -   **Crop**: Select a rectangular area on the image with your mouse to crop it.
    -   **Rotate**: Rotate the entire image 90 degrees counter-clockwise with a single click.
-   **Text Annotation**: Add custom text overlays onto the image. The application allows you to draw a rectangle to define the text area and choose a font color.
-   **Image Filters**: Apply a wide range of filters to alter the look and feel of your image. A dedicated window allows you to preview filters before applying them. Available filters include:
    -   Black and White
    -   Blur
    -   Sharpen
    -   Smooth
    -   Emboss
    -   Contour
    -   Edge Enhance
    -   Detail
-   **Canvas Management**:
    -   **Clear**: Revert all changes and restore the image to its original, unmodified state.
    -   **Aspect Ratio Preservation**: The application intelligently resizes images to fit the canvas while maintaining their original aspect ratio, preventing distortion.

## Technologies Used

-   **Python 3.x**
-   **Tkinter**: For the graphical user interface (GUI).
-   **Pillow (PIL Fork)**: The core library for all image manipulation tasks.

## Setup and Installation

Follow these steps to run the image editor on your local machine.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/ekrem-bas/Image-Editor.git
    cd image-editor
    ```

2.  **Create and activate a virtual environment (Recommended):**
    This isolates the project dependencies from your global Python installation.
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    The necessary library is listed in `requirements.txt`.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```sh
    python main.py
    ```

## How to Use

1.  **Open an Image**: Click the **"Add Image"** button to load a `.jpeg` or `.png` file.
2.  **Draw on the Image**:
    -   Click **"Draw"** to activate drawing mode. Click it again to deactivate.
    -   Use the **"Change Pen Color"** button to open a color picker.
    -   Adjust the **"Change Pen Size"** spinbox to set the brush thickness.
3.  **Crop the Image**:
    -   Click **"Crop"** to enter cropping mode.
    -   Click and drag your mouse over the image to draw a selection rectangle.
    -   Release the mouse button to perform the crop.
4.  **Add Text**:
    -   Click **"Add Text"** to enable text mode.
    -   Click and drag to draw a box where you want the text to appear.
    -   An input dialog will prompt you to enter your text.
    -   A color chooser will appear to let you select the font color.
5.  **Apply Filters**:
    -   Click the **"Select a filter"** button to open the filters menu.
    -   Click on any filter name to see a live preview on the canvas.
    -   Click **"Apply Filter"** to make the change permanent or **"Clear"** to revert.
6.  **Rotate**: Click the **"Rotate"** button to turn the image 90 degrees counter-clockwise.
7.  **Clear Changes**: Click the **"Clear"** button at any time to remove all edits and restore the original image.
8.  **Save the Image**: Click the **"Save"** button to open a file dialog and save your work as a new PNG or JPEG file.

## Screenshots

![1](https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/094865b0-e7cb-4ac8-a7b2-e2911f77bd1e)

![2](https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/1173752f-fb89-4cd4-8e12-fa8a8e70f015)

![3](https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/4e64a303-8d8f-4a43-b029-e92b572ded81)

![4](https://github.com/ekrem-bas/Basic-Image-Editor-Python-Project/assets/145195096/b1f37c91-887a-45ad-911a-a68eb4ecd06c)
