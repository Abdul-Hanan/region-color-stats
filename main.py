import cv2
import numpy as np
import os

def create_synthetic_image(width=300, height=200):
    """
    Creates a synthetic image with several distinct color blocks and a gradient.
    """
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # Define various solid color blocks (BGR format)
    # Blue block
    img[0:int(height/2), 0:int(width/2)] = [255, 0, 0]
    # Green block
    img[0:int(height/2), int(width/2):width] = [0, 255, 0]
    # Red block
    img[int(height/2):height, 0:int(width/3)] = [0, 0, 255]
    # Yellow block
    img[int(height/2):height, int(width/3):int(2*width/3)] = [0, 255, 255]

    # Create a gradient in the last section to ensure many distinct colors
    # (bottom-right region)
    grad_start_x = int(2*width/3)
    grad_start_y = int(height/2)
    grad_width = width - grad_start_x
    grad_height = height - grad_start_y

    for y in range(grad_height):
        for x in range(grad_width):
            # Create a unique BGR color for each pixel in the gradient region
            b = x % 256
            g = y % 256
            r = (x + y) % 256
            img[grad_start_y + y, grad_start_x + x] = [b, g, r]
            
    return img

def main():
    print("Starting region-color-stats project...")

    # 1. Create a synthetic image
    image = create_synthetic_image()
    image_height, image_width, _ = image.shape
    print(f"Synthetic image created: {image_width}x{image_height} pixels.")

    # 2. Define a rectangular region of interest (simulated click-and-drag)
    # These coordinates define a rectangle (x1, y1) to (x2, y2)
    # Chosen to overlap multiple solid color blocks and part of the gradient
    roi_x1, roi_y1 = 50, 50
    roi_x2, roi_y2 = 250, 150

    # Ensure ROI coordinates are within image bounds
    roi_x1 = max(0, roi_x1)
    roi_y1 = max(0, roi_y1)
    roi_x2 = min(image_width, roi_x2)
    roi_y2 = min(image_height, roi_y2)

    if not (roi_x1 < roi_x2 and roi_y1 < roi_y2):
        print("Error: Invalid ROI coordinates. Region is empty or inverted.")
        return

    print(f"Defined ROI: Top-Left ({roi_x1},{roi_y1}), Bottom-Right ({roi_x2},{roi_y2})")

    # 3. Extract the region of interest
    roi_image = image[roi_y1:roi_y2, roi_x1:roi_x2]

    # 4. Calculate the total count of distinct BGR colors
    # Reshape the ROI to a 2D array where each row is a BGR pixel
    pixels = roi_image.reshape(-1, 3)

    # Use numpy.unique to find distinct rows (i.e., distinct BGR colors)
    distinct_colors = np.unique(pixels, axis=0)
    distinct_color_count = len(distinct_colors)

    print(f"Calculated distinct BGR colors in the ROI: {distinct_color_count}")

    # 5. Prepare visual output: Draw the ROI and display the result on the image
    output_image = image.copy()
    
    # Draw the rectangle around the selected ROI
    cv2.rectangle(output_image, (roi_x1, roi_y1), (roi_x2, roi_y2), (0, 255, 255), 2) # Yellow color, 2px thickness

    # Add text to the image displaying the count
    text_result = f"Distinct BGR Colors: {distinct_color_count}"
    
    # Choose text position (top-left corner for visibility)
    text_pos = (10, 30) # (x, y)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    font_color = (255, 255, 255) # White
    font_thickness = 2
    
    cv2.putText(output_image, text_result, text_pos, font, font_scale, font_color, font_thickness)

    # 6. Save the visual output to a file
    output_filename = "output_region_color_stats.png"
    cv2.imwrite(output_filename, output_image)
    print(f"Output image saved to {output_filename}")

    print("Project finished successfully.")
    print("To view the results, open 'output_region_color_stats.png'.")

if __name__ == "__main__":
    main()