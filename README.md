# region-color-stats

Calculates the count of distinct BGR colors within a defined image region.

## Description

This project demonstrates a simple computer vision task using OpenCV and NumPy. It generates a synthetic image, defines a rectangular region of interest (ROI) programmatically, then calculates and displays the total number of distinct BGR color values present within that selected region. The visual output, including the drawn ROI and the color count, is saved to an image file.

*Note: Due to the requirement for headless execution (no GUI), the "click and drag" interaction is simulated by hardcoded ROI coordinates within the `main.py` script.*

## How to Run

1.  **Install Dependencies:**
    Make sure you have Python installed (3.7+ recommended). Then, install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Script:**
    Execute the main Python script:

    ```bash
    python main.py
    ```

## Output

After running the script, two things will happen:
1.  The console will print messages indicating the progress and the final count of distinct colors.
2.  An image file named `output_region_color_stats.png` will be created in the same directory. This image will show the generated synthetic image with the defined ROI highlighted by a yellow rectangle and the distinct color count displayed as text in the top-left corner.